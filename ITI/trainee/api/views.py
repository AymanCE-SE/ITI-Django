from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TraineeSerializer
from trainee.models import Trainee
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# with CBVs list and create
class TraineeListCreateAPIView(APIView):
    def get(self, request):
        trainees = Trainee.objects.all()
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# with GBVs update and delete
class TraineeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer