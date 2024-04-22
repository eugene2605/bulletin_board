from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.paginators import AdPaginator, CommentPaginator
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import AdSerializer, CommentSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('title',)

    def perform_create(self, serializer):
        new_ad = serializer.save(author=self.request.user)
        # new_ad.author = self.request.user
        new_ad.save()

    def get_permissions(self):
        if self.action in ('list',):
            self.permission_classes = [AllowAny,]
        elif self.action in ('create', 'retrieve'):
            self.permission_classes = [IsAuthenticated,]
        elif self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [IsOwner | IsAdmin]
        return super().get_permissions()


class AdMeListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    pagination_class = AdPaginator

    def get_queryset(self):
        user = self.request.user
        return Ad.objects.filter(author=user)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        new_comment = serializer.save(author=self.request.user, ad=Ad.objects.get(pk=self.kwargs['ad_pk']))
        new_comment.save()


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CommentPaginator
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        ad_pk = self.kwargs['ad_pk']
        return Comment.objects.filter(ad_id=ad_pk)


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        ad_pk = self.kwargs['ad_pk']
        return Comment.objects.filter(ad_id=ad_pk)


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsOwner | IsAdmin]

    def get_queryset(self):
        ad_pk = self.kwargs['ad_pk']
        return Comment.objects.filter(ad_id=ad_pk)


class CommentDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner | IsAdmin]

    def get_queryset(self):
        ad_pk = self.kwargs['ad_pk']
        return Comment.objects.filter(ad_id=ad_pk)
