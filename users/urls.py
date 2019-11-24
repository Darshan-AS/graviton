from rest_framework import routers

from users.apis.lender_api import LenderViewSet

router = routers.DefaultRouter()
router.register('api/lenders', LenderViewSet, 'lenders')

urlpatterns = router.urls
