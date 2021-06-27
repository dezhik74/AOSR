from django.urls import path

from .views import ObjectActsListView, ObjectActsSingleView

urlpatterns = [
    path('api/objects', ObjectActsListView.as_view(), name='objects_acts_list_view'),
    path('api/object/<int:pk>', ObjectActsSingleView.as_view(), name='objects_acts_single_view'),
]
