from rest_framework import routers

from users.apis.borrower_api import BorrowerViewSet
from users.apis.lender_api import LenderViewSet

router = routers.DefaultRouter()
router.register('api/lenders', LenderViewSet, 'lenders')
router.register('api/borrowers', BorrowerViewSet, 'borrowers')

urlpatterns = router.urls
