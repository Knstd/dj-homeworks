from django.urls import path

from measurement.views import SensorsView, MeasurementView, SensorUpdate

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
