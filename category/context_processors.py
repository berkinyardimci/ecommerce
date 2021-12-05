from .models import Category
#fatch all the categories from the database
#All Category area

def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)