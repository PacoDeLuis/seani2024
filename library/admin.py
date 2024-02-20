from django.contrib import admin

from .models import Module, Question

class QuestionInLine(admin.StackedInline):
    model = Question

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    inlines = [QuestionInLine]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'module', 'correct']
    ordering = ['module']

