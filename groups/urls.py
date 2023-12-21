from rest_framework import routers

from . import views

app_name = "groups"

router = routers.DefaultRouter()

router.register(prefix="groups", viewset=views.GroupViewSet, basename="group")
router.register(prefix="group-subscriptions", viewset=views.GroupPropertiesViewSet, basename="group-properties")

urlpatterns = router.urls
