from django.urls import path
from rest_framework.routers import DefaultRouter

from ads.apps import SalesConfig
from ads.views import AdViewSet, AdMeListAPIView, CommentListAPIView, CommentRetrieveAPIView, CommentCreateAPIView, \
    CommentUpdateAPIView, CommentDestroyAPIView


app_name = SalesConfig.name

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ad')

urlpatterns = [
    path('ads/me/', AdMeListAPIView.as_view(), name='ad-me'),

    path('ads/<int:ad_pk>/comments/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('ads/<int:ad_pk>/comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('ads/<int:ad_pk>/comments/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment-detail'),
    path('ads/<int:ad_pk>/comments/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='comment-update'),
    path('ads/<int:ad_pk>/comments/delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment-delete'),
] + router.urls
