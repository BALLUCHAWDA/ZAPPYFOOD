from django.contrib import admin
from ZappyFoodApp.models import User,AddProduct,Customer,Order

# Register your models here.
class AddProductAdmin(admin.ModelAdmin):
    list_display=['productName','productCategory','productPrice','productPics','productDescription','quantity']

admin.site.register(AddProduct,AddProductAdmin)

class UserAdmin(admin.ModelAdmin):
    #list_display='__all__'
    list_display=['username','password']
admin.site.register(User,UserAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer','customer_address','mobile']
    list_filter=['customer']
    list_editable=['mobile']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order)
