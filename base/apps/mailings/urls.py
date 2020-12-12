from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import ClientViewSet, MailDropViewSet, MailRecipientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
# generates:
# /clients/
# /clients/{pk}/

client_router = NestedDefaultRouter(router, r'clients', lookup='client')
client_router.register(r'maildrops', MailDropViewSet)
# generates:
# /clients/{client_pk}/maildrops/
# /clients/{client_pk}/maildrops/{maildrop_pk}/

maildrop_router = NestedDefaultRouter(client_router, r'maildrops', lookup='maildrop')
maildrop_router.register(r'recipients', MailRecipientViewSet)
# generates:
# /clients/{client_pk}/maildrops/{maildrop_pk}/recipients/
# /clients/{client_pk}/maildrops/{maildrop_pk}/recipients/{pk}/

# use re_path for regex-based routes, see docs below
# https://docs.djangoproject.com/en/3.0/ref/urls/#url
# https://docs.djangoproject.com/en/3.0/ref/urls/#re-path
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^', include(client_router.urls)),
    re_path(r'^', include(maildrop_router.urls)),
]
