from rest_framework.exceptions import UnsupportedMediaType
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework import status

from .models import Tip
from .serializers import TipSerializer



class TipListCreateView(APIView):

    def dispatch(self, request, *args, **kwargs):
        if request.content_type != 'application/json':
            raise UnsupportedMediaType('Only JSON content is allowed')
        return super().dispatch(request, *args, **kwargs)
    
    
    def get(self, request):
        tips = Tip.objects.all()
        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TipByLanguageView(APIView):
    
    def get(self, request, *args, **kwargs):
        language = self.kwargs.get('language')
        tips = Tip.objects.filter(language=language)
        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)



class TipSearchView(APIView):

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search', '')
        search_fields = ['title', 'description', 'language', 'tags']

        tips = Tip.objects.all()
        if search_query:
            query = Q()
            for field in search_fields:
                query |= Q(**{f'{field}__icontains': search_query}) 
            tips = tips.filter(query)

        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)