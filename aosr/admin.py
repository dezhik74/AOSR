from django.contrib import admin

from .models import ObjectActs, AOSR, AOSRFile

@admin.register(ObjectActs)
class ObjectActsAdmin(admin.ModelAdmin):
    pass


@admin.register(AOSR)
class AOSRAdmin(admin.ModelAdmin):
    pass


@admin.register(AOSRFile)
class AOSRFileAdmin(admin.ModelAdmin):
    pass


