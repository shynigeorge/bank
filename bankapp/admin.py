from django.contrib import admin

# Register your models here.


from bankapp.models import District, Register, City

admin.site.register(City)
admin.site.register(District)
admin.site.register(Register)
