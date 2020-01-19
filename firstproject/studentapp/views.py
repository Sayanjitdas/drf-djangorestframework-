from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers, StudentDetailedSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404

from rest_framework.views import APIView
# Create your views here.


class StudentListView(APIView):

    def get(self, request):

        students = Student.get_student.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'created successfully', 'data_created': serializer.data}, status=status.HTTP_201_CREATED)
        raise Http404


class StudentDetailedView(APIView):

    def get_object(self, pk):
        try:
            return Student.get_student.get(id=pk)
        except:
            return None

    def get(self, request, pk):

        student = self.get_object(pk)
        if student is not None:
            serializer = StudentDetailedSerializers(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise Http404

    def put(self, request, pk):
        student = self.get_object(pk)
        if student is not None:
            serializer = StudentDetailedSerializers(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'update successful'}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        if student is not None:
            student.delete()
            return Response({'msg': 'deleted successfully..'}, status.HTTP_204_NO_CONTENT)
        return Response(status.HTTP_400_BAD_REQUEST)

# function based

# @api_view(['GET', 'POST'])
# def student_list_view(request):

#     if request.method == 'GET':
#         query_student = Student.get_student.all()
#         serializer = StudentSerializers(query_student, many=True)
#         print(serializer)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentSerializers(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detailed_view(request, pk):
#     print(pk)
#     try:
#         student = Student.get_student.get(id=pk)
#     except Exception as e:
#         print(e)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = StudentDetailedSerializers(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = StudentDetailedSerializers(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'update success'}, status=status.HTTP_202_ACCEPTED)
#     elif request.method == 'DELETE':
#         student.delete()
#         return Response({'msg': 'request data deleted..'}, status=status.HTTP_204_NO_CONTENT)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
