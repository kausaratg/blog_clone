from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('post/<str:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create', views.PostCreateView.as_view(), name="post_create"),
    path('post/update/<str:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<str:pk>', views.PostDeleteView.as_view(), name='post_delete'),
    path('drafts', views.DraftListView, name='post_draft_list'),
    path('post/<str:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<str:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment<str:pk>/delete', views.comment_remove, name="comment_remove"),
    path('post/<str:pk>/publish', views.post_publish, name='post_publish')
]
