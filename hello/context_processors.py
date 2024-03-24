from . import models
def navbar_processor(request):
    
    categories = models.Category.objects.all()
    
    return {
        'categories': categories,
    }