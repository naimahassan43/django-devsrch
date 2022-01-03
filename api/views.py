
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectsSerializer
from projects.models import Projects

@api_view(['GET'])
def getRoutes(request):

   routes = [
      {'GET': '/api/projects'},
      {'GET': '/api/projects/id'},
      {'POST': '/api/projects/id/vote'},

      {'POST': '/api/users/token'},
      {'POST': '/api/users/token/refresh'},
   ]
   return Response(routes)

@api_view(['GET'])
def getProjects(request):
   projects = Projects.objects.all()
   serializer = ProjectsSerializer(projects, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
   project = Projects.objects.get(id=pk)
   serializer = ProjectsSerializer(project, many=False)
   return Response(serializer.data)