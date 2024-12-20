from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
from django.http import Http404
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer

class ProjectList(APIView):
   
   """
   return a list of all projects. Class base view
   """

   def get(self,request):
       projects = Project.objects.all()
       serializer = ProjectSerializer(projects, many=True)
       return Response(serializer.data)
   
   def post(self,request):
       serializer = ProjectSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(owner=request.user)
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED
           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )
   

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

"""
Retrieve a project by its pk
 """

class ProjectDetail(APIView):
   permission_classes = [
       permissions.IsAuthenticatedOrReadOnly,
       IsOwnerOrReadOnly

       ]

   def get_object(self, pk):
       try:
           project = Project.objects.get(pk=pk)
           self.check_object_permissions(self.request, project)
           return project
       except Project.DoesNotExist:
           raise Http404

   def get(self, request, pk):
       project = self.get_object(pk)
       serializer = ProjectDetailSerializer(project)
       return Response(serializer.data)
   
   def put(self, request, pk):
       project = self.get_object(pk)
       serializer = ProjectDetailSerializer(
           instance=project,
           data=request.data,
           partial=True
       )
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)

       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )
   

   
class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   # Only authenticated users can create pledges.


    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PledgeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            try:
                serializer.save()  # Supporter will automatically be set in serializer
                return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
            except Exception as e:
                print("Error during pledge creation:", str(e))
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        print("Serializer errors:", serializer.errors)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):  # provides detail and update functionality for individual pledges.
    permission_classes = [permissions.IsAuthenticated, IsSupporterOrReadOnly]

    def get_object(self, pk):  # retrieves the pledge by its primary key (pk), checks if the requester has permission, and raises a 404 error if the pledge doesn’t exist.
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):  #  uses the PledgeSerializer's update method to modify pledge data if the requester is the supporter.
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class PledgeDeleteView(generics.DestroyAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticated, IsSupporterOrReadOnly]
