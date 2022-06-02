from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note
from .serializer import NoteSerializer, QueryParamsSerializer


class NoteGetView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            get_model = Note.objects.order_by('-pub_date', '-important').filter(Q(author=request.user) | Q(public=True))
        else:
            get_model = Note.objects.order_by('-pub_date', '-important').filter(public=True)
        query_params = QueryParamsSerializer(data=request.query_params)
        if query_params.is_valid():
            if query_params.data.get('important'):
                get_model = get_model.filter(important__in=query_params.data['important'])
            if query_params.data.get('public'):
                get_model = get_model.filter(public__in=query_params.data['public'])
            if query_params.data.get('state'):
                get_model = get_model.filter(state__in=query_params.data['state'])
        else:
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = NoteSerializer(get_model, many=True)
        return Response(serializer.data)


class NoteDetailedGetView(APIView):
    def get(self, request, note_id):
        if request.user.is_authenticated:
            new_model = Note.objects.filter(Q(author=request.user) & Q(pk=note_id))
        else:
            new_model = Note.objects.filter(Q(pk=note_id) & Q(public=True))
        if not new_model:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(new_model, many=True)
        return Response(serializer.data)

class NotePostView(APIView):
    def post(self, request):
        new_model = NoteSerializer(data=request.data)
        if new_model.is_valid():
            new_model.save(author=request.user)
            return Response(new_model.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_model.errors, status=status.HTTP_400_BAD_REQUEST)


class NotePatchView(APIView):
    def patch(self, request, note_id):

        model = Note.objects.filter(pk=note_id, author=request.user).first()
        if not model:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(model, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class NoteDeleteView(APIView):
    def delete(self, request, note_id):
        model = Note.objects.filter(pk=note_id, author=request.user)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class AboutTemplateView: # todo страница about
#     """https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#django.views.generic.base.TemplateView"""
#     pass

def about(request):
    params = {
        'user': request.user,
        'version': settings.SERVER_VERSION
    }
    return render(request, 'about.html', params)