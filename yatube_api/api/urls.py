from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = DefaultRouter()
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='GroupViewSet')
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include('djoser.urls')),
    path('v1/', include(router.urls)),
]
