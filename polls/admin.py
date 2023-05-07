from django.contrib import admin

# Register your models here.
from .models import Question, Choice


# style can be changed by replacing the TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # like query
    search_fields = ["question_text"]
    # filter by
    list_filter = ["pub_date"]
    # 列表展示的样子
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # fields分块展示
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    # fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)

