from django.db import models
from datetime import date  
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 

today= date.today()

Category_Choices = (
    ('Tech', 'Tech'),
    ('Fashion', 'Fashion'),
    ('Entertainment', 'Entertainment'),
    ('Politics', 'Politics'),
)

Status = (  
    ('Draft','Draft'),
    ('Publish','Publish')
)

#BlogPost class 
class BlogPost(models.Model):
    title = models.CharField(max_length=50 , null=False, blank=False)
    slug = models.SlugField()
    preface = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=50, choices=Category_Choices,
                default='Tech')
    image = models.ImageField(upload_to=f"photos/{today}", null=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=Status, default='Draft')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}--{self.created_by}"



