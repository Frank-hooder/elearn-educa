from django.contrib import admin
from .models import Subject, Course, Module, Ad, Ads_images, Company

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}
class ModuleInline(admin.StackedInline):
	model = Module
	extra = 4

class Ads_imagesInline(admin.StackedInline):
	model = Ads_images
	extra = 3

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
	list_filter = ['created', 'title']
	prepopulated_fields = {'slug': ('title',)}
	inlines = [Ads_imagesInline]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'subject', 'created']
	list_filter = ['created', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('title',)}
	inlines = [ModuleInline]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('company_name',)}