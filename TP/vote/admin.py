from django.contrib import admin
from models import V_event,V_chioce,Cat


class V_eventAdmin(admin.ModelAdmin):
    list_display=('event_discribe','event_pic','pu_date','end_date')

class V_chioceAdmin(admin.ModelAdmin):
    list_display=('choice_detail','count','choice_pic')
    
    
class CatAdmin(admin.ModelAdmin):
    list_display=('category_name')


admin.site.register(V_event,V_eventAdmin)
admin.site.register(V_chioce,V_chioceAdmin)
admin.site.register(Cat)