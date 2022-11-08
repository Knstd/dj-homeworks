from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Relationship, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag = 0
        for form in self.forms:
            for key, value in form.cleaned_data.items():
                if key == 'is_main' and value:
                    main_tag += 1
        if main_tag > 1:
            raise ValidationError('Не может быть двух главных разделов')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    list_display = ('id', 'title', 'text', 'published_at', 'image')
    list_display_links = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
