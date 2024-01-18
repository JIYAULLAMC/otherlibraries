from django.urls import path
# from .views import StudentListView, StudentDetailView, ContactFormView, StudentCreateView, StudentUpdateView, StudentDeleteView
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    title="My API",
    description = "api for the blog",
    permission_classes=(AllowAny,),  # Adjust permissions as needed
)

urlpatterns = [
    # path("students/", StudentListView.as_view(), name="students"),
    # path("student/<int:pk>/", StudentDetailView.as_view(), name="student"),

    # ##########################################################
    # # Edit Class Base View
    # path("contact/", ContactFormView.as_view(), name="contact"),

    # # Create class base view
    # path("create/", StudentCreateView.as_view(),name="student_create"),

    # # update class base generic view
    # path("update/<int:pk>/", StudentUpdateView.as_view(), name="student_update"),
    # path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student_update"),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),
    path('docs/', include_docs_urls(title='Your API Documentation')),

]
