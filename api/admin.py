from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models.user import User
from .models.mango import Mango

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['id', 'email', 'is_superuser', 'last_login']
    # The fieldsets are used when you edit a new user via the admin site.
    # fieldsets is a list in the form of two tuples, where each pair represents an
    # html <fieldset> on the admin page.  The tuples are in the format:
    # (name, field_options), where name is a string representing the title of
    # the fieldset and field_options is a dictionary of information about the
    # fieldset including the list of fields.
    # Below we're saying create 4 sections, the first section has no name specified
    fieldsets = (
      (None, {'fields': ('email', 'password')}),
      ('Permissions',
          {
              'fields': (
                  'is_active',
                  'is_staff',
                  'is_superuser',
              )
          }
      ),
      ('Dates', {'fields': ('last_login',)}),
    )
    # add_fieldsets is similar to fieldsets but it is used specifically
    # when you create a new user:
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

# register the model and tell Django to use the above UserAdmin
# class to format the pages:
admin.site.register(User, UserAdmin)
admin.site.register(Mango)
