from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer
from .paginations import MyPagination
from .models import Student
from .filters import StudentFilter
from rest_framework.throttling import ScopedRateThrottle
from django.shortcuts import get_object_or_404
from rest_framework import status

class StudentAPI(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'student_throttle' 

    def get(self, request):
        queryset = Student.objects.all()
        filterset = StudentFilter(request.query_params, queryset=queryset)
        paginator = MyPagination()
        paginated_queryset = paginator.paginate_queryset(filterset.qs,request)
        
        data = [
            {
                "id": obj.id,
                "Name": obj.Name,
                "F_name": obj.F_name,
                "M_name": obj.M_name,
                "p_no": obj.p_no,
                "course": obj.course,
                "roll": obj.roll,
                "age": obj.age
            } for obj in paginated_queryset
        ]
        return paginator.get_paginated_response(data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.create(serializer.validated_data)
            return Response({
                "id": student.id,
                "Name": student.Name,
                "F_name": student.F_name,
                "M_name": student.M_name,
                "p_no": student.p_no,
                "course": student.course,
                "roll": student.roll,
                "age": student.age
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        obj = get_object_or_404(Student, id=request.data.get('id'))
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            student = serializer.update(obj, serializer.validated_data)
            return Response({
                "id": student.id,
                "Name": student.Name,
                "F_name": student.F_name,
                "M_name": student.M_name,
                "p_no": student.p_no,
                "course": student.course,
                "roll": student.roll,
                "age": student.age
            }, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request):
        obj = get_object_or_404(Student, id=request.data.get('id'))
        serializer = StudentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            student = serializer.update(obj, serializer.validated_data)
            return Response({
                "id": student.id,
                "Name": student.Name,
                "F_name": student.F_name,
                "M_name": student.M_name,
                "p_no": student.p_no,
                "course": student.course,
                "roll": student.roll,
                "age": student.age
            }, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        data = request.data
        obj = get_object_or_404(Student,id=data.get('id'))
        obj.delete()
        return Response({'message': 'Student deleted successfully'}, status=200)
