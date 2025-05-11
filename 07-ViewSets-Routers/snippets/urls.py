# without routers

# from rest_framework import renderers
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from django.urls import path
# snippet_list = SnippetViewSet.as_view(
#     {
#         "get": "list",
#         "post": "create",
#     }
# )
# snippet_detail = SnippetViewSet.as_view(
#     {
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy",
#     }
# )
# snippet_highlight = SnippetViewSet.as_view(
#     {
#         "get": "highlight",
#     },
#     renderer_classes=[renderers.StaticHTMLRenderer],
#     name="snippet-highlight",
# )
# user_list = UserViewSet.as_view(
#     {
#         "get": "list",
#     }
# )
# user_detail = UserViewSet.as_view(
#     {
#         "get": "retrieve",
#     }
# )

# urlpatterns = [
#     path("", api_root, name="api-root"),
#     path("snippets/", snippet_list, name="snippet-list"),
#     path("snippets/<int:pk>/", snippet_detail, name="snippet-detail"),
#     path("snippets/<int:pk>/highlight/", snippet_highlight, name="snippet-highlight"),
#     path("users/", user_list, name="user-list"),
#     path("users/<int:pk>/", user_detail, name="user-detail"),
# ]


from rest_framework.routers import DefaultRouter
from django.urls import path, include
from snippets import views

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet)
router.register(r"users", views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]