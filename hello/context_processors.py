from . import models
def navbar_processor(request):
    
    categories = models.Category.objects.all()
    subcategories = models.Subcategory.objects.all()
    
    return {
        'categories': categories,
        'subcategories': subcategories,
    }