from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    # Imported and added the permissions here to prevent other viewers from updating or deleting the data, just view.
    # Only author has the permission
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # Imported and added the permissions here to prevent other viewers from updating or deleting the data, just view.
    # Only author has the permission
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer