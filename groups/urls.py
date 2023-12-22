from rest_framework import routers

from . import views

app_name = "groups"

router = routers.DefaultRouter()

router.register(prefix="property-membership", viewset=views.GroupPropertiesViewSet, basename="group-properties")
router.register(prefix="", viewset=views.GroupViewSet, basename="group")

urlpatterns = router.urls
