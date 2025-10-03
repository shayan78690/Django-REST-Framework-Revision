# import django_filters
# from .models import Employee

# class EmployeeFilter(django_filters.FilterSet):
#     designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    
#     class Meta:
#         model = Employeea
#         fields = ['designation']  # Correct: flat list
# import django_filters
# from .models import Employee

# class EmployeeFilter(django_filters.FilterSet):
#     designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
#     emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    
#     class Meta:
#         model = Employee
#         fields = ['designation', 'emp_name']  # Correct: flat list
# import django_filters
# from .models import Employee

# class EmployeeFilter(django_filters.FilterSet):
#     designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
#     emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
#     id = django_filters.RangeFilter(field_name='id')
    
#     class Meta:
#         model = Employee
#         fields = ['designation', 'emp_name', 'id']  

import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label ='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To EMP ID')
    
    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id_min', 'id_max'] 
    
    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            queryset.filter(emp_id__lte=value)
        return queryset