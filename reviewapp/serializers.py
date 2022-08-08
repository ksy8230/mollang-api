from rest_framework import serializers
from reviewapp.models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.name')
    class Meta:
        model = Comment
        fields = ('id', 'review', 'comment', 'created_at', 'username')
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.name')
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)  # 댓글 갯수
    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        company = Review.objects.create(**validated_data)
        return company

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.categories = validated_data.get("categories", instance.categories)
    #     instance.region = validated_data.get("region", instance.region)
    #     instance.phone = validated_data.get("phone", instance.phone)
    #     instance.siteUrl = validated_data.get("siteUrl", instance.siteUrl)
    #     instance.save()
    #     return instance

