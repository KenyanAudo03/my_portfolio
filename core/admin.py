from django.contrib import admin
from .models import HomepageHero, HeroPhrase


class HeroPhraseInline(admin.TabularInline):
    model = HeroPhrase
    extra = 1  # show 1 empty row for quick adding
    ordering = ["order"]


@admin.register(HomepageHero)
class HomepageHeroAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "is_active")
    list_filter = ("is_active",)
    inlines = [HeroPhraseInline]


@admin.register(HeroPhrase)
class HeroPhraseAdmin(admin.ModelAdmin):
    list_display = ("text", "hero", "order")
    list_filter = ("hero",)
    ordering = ["hero", "order"]
