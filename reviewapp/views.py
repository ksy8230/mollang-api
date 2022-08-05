from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from reviewapp.serializers import ReviewSerializer
from reviewapp.models import Review
from rest_framework.generics import get_object_or_404

# 리뷰 등록 / 리뷰 수정 / 리뷰 삭제 / 리뷰 상세보기
class RegisterReview(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


# 리뷰 리스트 조회
class ReviewList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        queryset = Review.objects.order_by("-updated_at", "-id")
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

