from django.contrib import admin
from . import models
# Register your models here.

#to utilize admin interface to edit models as same page as parent model

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
