from django.http import JsonResponse
from django.urls import path
from cart_update import update_cart
from rotate_profile import rotate_profile
from annotate_promotion import annotate_promotion
from publish_config import publish_config
from reconcile_bundle import reconcile_bundle
from render_header import render_header
from validate_schedule import validate_schedule


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("update_cart", update_cart),
    path("rotate_profile", rotate_profile),
    path("annotate_promotion", annotate_promotion),
    path("publish_config", publish_config),
    path("reconcile_bundle", reconcile_bundle),
    path("render_header", render_header),
    path("validate_schedule", validate_schedule),
]
