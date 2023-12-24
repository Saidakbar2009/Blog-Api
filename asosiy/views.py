from django.shortcuts import render
from .serialers import *
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *
# Create your views here.
class MaqolalarModelViewSet(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        muallif = Maqola.objects.all()
        serializer = MaqolaModelSerializer(muallif, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        maqolalar = request.data
        serializer = MaqolalarModelViewSet(maqolalar)
        if serializer.is_valid():
            Maqola.objects.create(
                serializer.save(Muallif=request.user)
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class MaqolaApiView(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        maqola = Maqola.objects.get(id=pk)
        serializer = MaqolalarModelViewSet(maqola)
        maqola.korish_soni += 1
        return Response(serializer.data)

    def update(self, request, pk):
        maqola = Maqola.objects.get(id=pk)
        serializer = MaqolaModelSerializer(maqola)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        Maqola.objects.get(id=pk).delete()
        return Response({"success": "True"})