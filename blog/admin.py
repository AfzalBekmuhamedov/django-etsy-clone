from django.contrib import admin
from blog.models import *

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)


