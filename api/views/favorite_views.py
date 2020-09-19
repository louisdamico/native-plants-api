from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.favorite import Favorite
from ..serializers import FavoriteSerializer, UserSerializer

# Create your views here.
class Favorites(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = FavoriteSerializer
    def get(self, request):
        """Index request"""
        # Get all the favorite:
        # favorite = Favorite.objects.all()
        # Filter the favorite by owner, so you can only see your owned mangos
        favorite = Favorite.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = FavoriteSerializer(favorite, many=True).data
        return Response({ 'favorite': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['favorite']['owner'] = request.user.id
        # Serialize/create favorite
        favorite = FavoriteSerializer(data=request.data['favorite'])
        # If the favorite data is valid according to our serializer...
        if favorite.is_valid():
            # Save the created favorite & send a response
            favorite.save()
            return Response({ 'favorite': favorite.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(favorite.errors, status=status.HTTP_400_BAD_REQUEST)

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        favorite = get_object_or_404(Favorite, pk=pk)
        # Only want to show owned mangos?
        if not request.user.id == favorite.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this list')

        # Run the data through the serializer so it's formatted
        data = FavoriteSerializer(favorite).data
        return Response({ 'favorite': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate favorite to delete
        favorite = get_object_or_404(Favorite, pk=pk)
        # Check the favorite's owner agains the user making this request
        if not request.user.id == favorite.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this list')
        # Only delete if the user owns the  mango
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['mango'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['favorite'].get('owner', False):
            del request.data['favorite']['owner']

        # Locate List
        # get_object_or_404 returns a object representation of our Mango
        favorite = get_object_or_404(Favorite, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == favorite.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this list')

        # Add owner to data object now that we know this user owns the resource
        request.data['favorite']['owner'] = request.user.id
        # Validate updates with serializer
        data = FavoriteSerializer(favorite, data=request.data['favorite'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
