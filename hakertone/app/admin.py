from django.contrib import admin
from .models import User_info, Company, Group_buying, Group_buying_comment, Flee_market
# Register your models here.
admin.site.register(User_info)
admin.site.register(Company)
admin.site.register(Group_buying)
admin.site.register(Group_buying_comment)
admin.site.register(Flee_market)
