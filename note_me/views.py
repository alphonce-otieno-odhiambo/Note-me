from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Note
from .serializers import  NoteSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint': '/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single note'
        },
        {
            'Endpoint': '/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates new note with data sent with post'
        },
        {
            'Endpoint': '/notes/id/update',
            'method':'PUT',
            'body':{'body':""},
            'description':'Create an existing note with data sent in post'
        },
        {
            'Endpoint': '/notes/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing note'
        },

    ]
    return Response(routes )

@api_view(['GET'])
def getNotes(request):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)
   
@api_view(['GET'])
def note(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)