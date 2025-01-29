from django.contrib import admin
from .models import Tweet, Like
from django.db.models import Q


class TweetCustomFilter(admin.SimpleListFilter):
    title = "likes"
    parameter_name = "likes"

    def lookups(self, request, model_admin):
        return (
            ("elon musk contains", "elon musk"),
            ("not musk", "not musk"),
        )
    
    def queryset(self, request, queryset):
        if (self.value() == "elon musk contains"):
            return queryset.filter(content__contains="elon musk")
        elif (self.value() == "not musk"):
            return queryset.filter(~Q(content__contains="elon musk"))
        

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    readonly_fields = ("likes_count", "created_at")
    list_display = ("content", "user", "likes_count")
    search_fields = ("content", "user__username",)
    list_filter = (TweetCustomFilter, "user", "created_at")



@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet")
    list_filter = ("created_at", "user", "tweet")
    search_fields = ("user__username", )
