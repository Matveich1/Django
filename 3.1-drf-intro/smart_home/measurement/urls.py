from django.urls import path


from .views import SensorList, SensorInfo, Measurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorList.as_view()),
    path('sensors/<int:pk>/', SensorInfo.as_view()),
    path('measurements/', Measurement.as_view()),
]
