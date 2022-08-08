from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from reviewapp.serializers import ReviewSerializer, CommentSerializer
from reviewapp.models import Review, Comment
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

# 리뷰 > 등록 / TODO : 리뷰 수정 / 리뷰 삭제
class RegisterReview(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 리뷰 > 상세 보기
class UpdateReview(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        review = get_object_or_404(Review, pk=pk)
        return review

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        single_review = self.get_object(pk)
        serializer = ReviewSerializer(instance=single_review)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 리뷰 > 리스트 조회
class ReviewList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        queryset = Review.objects.order_by("-updated_at", "-id")
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 댓글 > 등록 / TODO : 댓글 수정 / 댓글 삭제
class RegisterComment(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        review = get_object_or_404(Review, pk=pk)
        return review
    def get_comment_object(self, pk):
        comment = get_object_or_404(Comment, pk=pk)
        return comment

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        review = self.get_object(pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(review=review, username=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        comment_pk = self.kwargs.get('comment_pk')
        saved_comment = self.get_comment_object(comment_pk)
        serializer = CommentSerializer(instance=saved_comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


