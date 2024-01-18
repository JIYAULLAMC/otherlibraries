# from django.shortcuts import render
# from django.views.generic.list import ListView
# from .models import Student
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
# from .forms import ContactForm, StudentForm
# from django import forms



# students/views.py
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# class StudentListView(ListView):
#     model = Student
#     template_name = "school/student.html"

#     # context_object_name = 'students'

#     # def get_queryset(self):
#     #     qs = super().get_queryset()
#     #     return qs.filter(roll=101)

#     # def get_context_data(self, *args, **kwargs):
#     #     context = super().get_context_data(*args, **kwargs)
#     #     print("----------------------------------")
#     #     print(context)
#     #     context["vishwas"] = Student.objects.filter(name='vishwa')
#     #     print(context)
#     #     return context

#     def get_template_names(self):
#         # you have to validate this by seting the cookie in browser name 'user' vlaue 'sonam'

#         if self.request.COOKIES['user'] == 'sonam':
#             # if self.request.user.is_superuser:  different condition to render the template
#             # if self.request.user.is_superuser:
#             # if self.request.user.is_superuser:
#             template_name = 'school/sonam.html'
#         else:
#             template_name = self.template_name

#         return [template_name]


# # Detail View


# class StudentDetailView(DetailView):
#     model = Student


# ##########################################################
# # Edit Class Base View


# class ContactFormView(FormView):
#     template_name = "school/contact.html"
#     form_class = ContactForm
#     success_url = "/students/"
#     initial = {
#         "name": "jiyaulla"
#     }

#     def form_valid(self, form):
#         # print("------------------", form)
#         print("-------------", form.__dict__)
#         # we can extract the data
#         print("-----------", form.cleaned_data['name'])
#         return super().form_valid(form)


# class StudentCreateView(CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = "school/student_form.html"
#     success_url = "/students/"


# class StudentUpdateView(UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = "school/student_form.html"
#     success_url = "/students/"


# class StudentDeleteView(DeleteView):
#     model = Student
#     success_url = "/students/"




