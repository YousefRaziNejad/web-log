from django.urls import path

from blog.views import post_list, post_detail, post_create, post_update, post_delete, category_detail, post_search, add_comment

urlpatterns = [
    path("post/list/", post_list, name="post-list"),
    path("post/detail/<int:id>/", post_detail, name="post-detail"),
    path("post/create/", post_create, name="post-create"),
    path("post/detail/<int:id>/update/", post_update, name="post-update"),

    path("post/detail/<int:id>/delete/", post_delete, name="post-delete"),
    path("post/search/", post_search, name="post-search"),

    path("post/detail/<int:id>/comment/", add_comment, name="add-comment"),
    path("category/<int:id>/", category_detail, name="category-detail"),
]
