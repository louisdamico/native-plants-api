from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    """Manager for user profiles"""

    # The create_user method is passed:
    # self:      All methods in Python receive the class as the first argument
    # email:     Because we want to be able to log users in with email
    #            instead of username (Django's default behavior)
    # password:  The password has a default of None for validation purposes.
    #            This ensures the proper error is thrown if a password is
    #            not provided.
    # **extra_fields:  Just in case there are extra arguments passed.
    def create_user(self, email, password=None, **extra_fields):
        """Create a new user profile"""
        # Add a custom validation error
        if not email:
            raise ValueError('User must have an email address')

        # Create a user from the UserModel
        # Use the normalize_email method from the BaseUserManager to
        # normalize the domain of the email
        # We'll also unwind the extra fields.  Remember that two asterisk (**)
        # in Python refers to the extra keyword arguments that are passed into
        # a function (meaning these are key=value pairs).
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # Use the set_password method to hash the password
        user.set_password(password)
        # Call save to save the user to the database
        user.save()

        # Always return the user!
        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser with given details"""

        # Use the custom create_user method above to create
        # the user.
        user = self.create_user(email, password)

        # Add the required is_superuser and is_staff properties
        # which must be set to True for superusers
        user.is_superuser = True
        user.is_staff = True
        # Save the user to the database with the new properties
        user.save()

        # Always return the user!
        return user

# Inherit from AbstractBaseUser and PermissionsMixin:
class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users"""
    # As with any Django models, we need to define the fields
    # for the model with the type and options:
    email = models.EmailField(max_length=255, unique=True)
    # name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Any time we call User.objects (such as in objects.all() or objects.filter())
    # make sure to use the custom user manager we created.
    objects = UserManager()

    # Tell Django to use the email field as the unique identifier for the
    # user account instead of its built in behavior of using the username.
    USERNAME_FIELD = 'email'
    # This doesn't mean the field is required (that's defined above in the field options)
    # This refers to the fields that are prompted for when creating a superuser.
    # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    # REQUIRED_FIELDS = ['name']

    # Standard Python: We'll create a string representation so when
    # the class is output we'll get something meaningful.
    def __str__(self):
        """Return string representation of the user"""
        return self.email

    def get_auth_token(self, obj):
        Token.objects.filter(user=obj).delete()
        token = Token.objects.create(user=obj)
        obj.token = token.key
        obj.save()
        return token.key

    def delete_token(self, obj):
        Token.objects.filter(user=obj).delete()
        obj.token = None
        obj.save()
        return obj
