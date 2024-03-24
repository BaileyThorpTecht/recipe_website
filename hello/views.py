from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models

class LandingView(ListView):
    model = models.Feedback
    template_name = 'hello/landing.html'
    context_object_name = 'feedback'

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = models.Feedback
    fields = ['title', 'description']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryView(ListView):
    model = models.Subcategory
    template_name = 'hello/recipe_category.html'
    context_object_name = 'subcategories'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['cat'] = self.request.path.split("/")[2]
        return context

class SubcategoryView(ListView):
    model = models.Recipe
    template_name = 'hello/recipe_subcategory.html'
    context_object_name = 'recipes'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['subcat'] = self.request.path.split("/")[3]
        return context
    
class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'hello/allrecipes.html'
    context_object_name = 'recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe    
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('landing')
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'subcategory']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NavbarView(ListView):
    model = models.Category
    template_name = 'recipes/base.html'
    context_object_name = 'categories'