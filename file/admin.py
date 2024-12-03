from django.contrib import admin

# Register your models here.
from django.contrib import admin
from file.models import Member,Learn,Akshada,Fil,Mohan
# from file.models import Comment


class users(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'password')



class fil(admin.ModelAdmin):
    list_display = ('file',)



class lusers(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'courses','gender')


class mohan(admin.ModelAdmin):
    list_display = ('id','name' )



class akshada(admin.ModelAdmin):
    list_display = ('aname', 'aemail', 'aissue', 'aremark','aservice')

admin.site.register(Member,users)    
admin.site.register(Learn,lusers)    
admin.site.register(Akshada,akshada) 
admin.site.register(Fil,fil)
admin.site.register(Mohan,mohan)
# admin.site.register(Comment)