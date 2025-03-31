import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    Name = django_filters.CharFilter(field_name='Name', lookup_expr='icontains')
    F_name = django_filters.CharFilter(field_name='F_name', lookup_expr='icontains')
    M_name = django_filters.CharFilter(field_name='M_name', lookup_expr='icontains')
    p_no = django_filters.NumberFilter(field_name='p_no')
    course = django_filters.CharFilter(field_name='course', lookup_expr='icontains')
    roll = django_filters.NumberFilter(field_name='roll')  
    age = django_filters.NumberFilter(field_name='age')

    class Meta:
        model = Student
        fields = ['Name', 'F_name', 'M_name', 'p_no', 'course', 'roll', 'age'] #not include id
