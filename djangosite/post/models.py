from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class Articles(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.CharField(max_length=500, blank=False, null=False)
    last_update = models.DateField(auto_now=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='articles_related_tags'
    )


def _get_articles():
    return Articles.objects.all().order_by('-last_update')

def _get_articles_by_id(id):
    return Articles.objects.filter(id=id).first()

def _create_articles(request):
    a = Articles.objects.create(user=request.user, title=request.POST['title'], content=request.POST['content'])
    query = dict(request.POST)
    for i in query['tags']:
        a.tags.add(Tag.objects.get(id=i))
    return

def _edit_articles_by_id(request,id):
    Articles.objects.filter(id=id).update(title=request.POST['title'], content=request.POST['content'])
    a = Articles.objects.filter(id=id).get()
    a.tags.remove()
    query = dict(request.POST)
    for i in query['tags']:
        a.tags.add(Tag.objects.get(id=i))
    return

def _del_articles_by_id(id):
    Articles.objects.filter(id=id).delete()
    return

