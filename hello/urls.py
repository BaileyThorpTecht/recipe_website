from django.urls import path
from hello import views

urlpatterns = [
    path("", views.LandingView.as_view(), name="landing"),
    path("feedback/", views.FeedbackCreateView.as_view(), name="feedback-create"),
    path("recipes/", views.RecipeListView.as_view(), name="recipe-all"),
    path("recipe/<int:pk>", views.RecipeDetailView.as_view(), name="recipe-detail"),
    path("recipe/create", views.RecipeCreateView.as_view(), name="recipe-create"),
    path("recipe/<int:pk>/update", views.RecipeUpdateView.as_view(), name="recipe-update"),
    path("recipe/<int:pk>/delete", views.RecipeDeleteView.as_view(), name="recipe-delete"),
    path("recipe/search", views.SearchView.as_view(), name="recipe-search"),
    path("recipe/<a>", views.CategoryView.as_view(), name="recipe-category"),
    path("recipe/<a>/<b>", views.SubcategoryView.as_view(), name="recipe-subcategory"),
     
]
