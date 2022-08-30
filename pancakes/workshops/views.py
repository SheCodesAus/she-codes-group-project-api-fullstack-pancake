from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Workshop
from .serializers import WorkshopSerializer, WorkshopDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOrganiserOrReadOnly

# /workshops
class WorkshopList(APIView):
    # GET request
    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data)

    # POST request
    def post(self, request):
        # if not request.user.is_authenticated:
        #     return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WorkshopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organiser=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class WorkshopDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOrganiserOrReadOnly
    ]
    
    # def get_object(self, pk):
    #     try:
    #         workshop = Workshop.objects.get(pk=pk) 
    #         self.check_object_permissions(self.request,workshop)
    #         return workshop  
    #     except Workshop.DoesNotExist:
    #         raise Http404

    def get_object(self, pk):
        return Workshop.objects.get(pk=pk)

    # GET request    
    def get(self, request, pk):
        workshop = self.get_object(pk)
        # serializer = WorkshopDetailSerializer(workshop)
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)