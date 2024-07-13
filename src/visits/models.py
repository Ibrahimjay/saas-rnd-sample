from django.db import models

# Create your models here.
class page_visit(models.Model):
    # db -> table
    # id -> hidden -> primarykey  -> autofield -> 1,2,3,4,5,6
    path = models.TextField(blank=True, null=True) # col
    timestamp = models.DateTimeField( auto_now_add=True) #col
