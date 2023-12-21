from rest_framework import routers

from . import views

app_name = "properties"

router = routers.DefaultRouter()

router.register(prefix="locations", viewset=views.LocationViewSet, basename="location")
router.register(prefix="", viewset=views.PropertyViewSet, basename="property")

urlpatterns = router.urls
