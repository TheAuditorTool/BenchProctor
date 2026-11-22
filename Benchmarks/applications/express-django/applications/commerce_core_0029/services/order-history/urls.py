from django.http import JsonResponse
from django.urls import path
from order_lookup import lookup_order
from publish_promotion import publish_promotion
from validate_header import validate_header
from collect_fulfillment import collect_fulfillment
from rotate_fulfillment import rotate_fulfillment
from enrich_profile import enrich_profile
from format_header import format_header


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("lookup_order", lookup_order),
    path("publish_promotion", publish_promotion),
    path("validate_header", validate_header),
    path("collect_fulfillment", collect_fulfillment),
    path("rotate_fulfillment", rotate_fulfillment),
    path("enrich_profile", enrich_profile),
    path("format_header", format_header),
]
