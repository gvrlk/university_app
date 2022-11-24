from rest_framework import viewsets, generics, mixins, response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.db.models import Sum, Max, F

from education_app.models import Work, Assessment

from .serializers import WorkSerializer, AssessmentSerializer, UserSerializer


# Create your views here.
class WorkViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    @action(methods=['get'], detail=False, url_path='best-works')
    def best_works(self, request):
        works = (
            Work.objects
                .annotate(score_sum=Sum('assessments__score'))
                .order_by('-score_sum')[:3]
        )
        serializer = WorkSerializer(works, many=True)
        return response.Response(data=serializer.data)


# class AssessmentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class WorkList(generics.ListCreateAPIView):
#     queryset = Work.objects.all()
#     serializer_class = WorkSerializer
#
#
# class WorkDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Work.objects.all()
#     serializer_class = WorkSerializer

# class WorkList(views.APIView):
#
#     def get(self, request, format=None):
#         objects = Work.objects.all()
#         serializer = WorkSerializer(objects, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = WorkSerializer(data=request.data)
#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class WorkDetail(views.APIView):
#
#     def get(self, request, pk, format=None):
#         _object = get_object_or_404(Work, pk=pk)
#         serializer = WorkSerializer(_object)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         _object = get_object_or_404(pk)
#         serializer = WorkSerializer(_object, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         _object = get_object_or_404(pk)
#         _object.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
