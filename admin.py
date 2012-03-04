from django.contrib import admin
from models import *

class ProjectImageInline(admin.StackedInline):
    model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ]
    prepopulated_fields = {"url": ("headline",)}

class ReferenceImageInline(admin.StackedInline):
    model = ReferenceImage

class ReferenceAdmin(admin.ModelAdmin):
    inlines = [ReferenceImageInline, ]
    prepopulated_fields = {"url": ("headline",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Reference, ReferenceAdmin)
