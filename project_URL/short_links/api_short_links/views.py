from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from .models import Url
from .utils import hash_url
from .serializer import UrlSerializer


# saves the user's entry into the database and which will create the object
@api_view(['POST'])
def short_url(request):
    if request.method == 'POST':
        long_url = request.data.get('long_url')
        short_url = hash_url(long_url)

        obj = Url.objects.create(long_url=long_url, short_url=short_url)
        serializer = UrlSerializer(obj)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# function that redirects user to long URL
def redirect_long_url(request, short_url):
    obj = Url.objects.get(short_url=short_url)
    obj.track()
    return redirect(obj.long_url)


# retrieve data associated with the short URL
@api_view(['GET'])
def retrive_short_url_details(request, short_url):
    try:
        url = Url.objects.get(short_url=short_url)
        serializer = UrlSerializer(url)
        return Response(serializer.data)
    except Url.DoesNotExist:
        return Response({"error": "Short URL not found"},
                        status=status.HTTP_404_NOT_FOUND)
