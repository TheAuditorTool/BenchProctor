from django.http import JsonResponse
from django.urls import path
from cart_update import update_cart
from collect_policy import collect_policy
from format_manifest import format_manifest
from archive_manifest import archive_manifest
from publish_schedule import publish_schedule
from compact_cart import compact_cart
from compact_manifest import compact_manifest
from validate_order import validate_order


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("update_cart", update_cart),
    path("collect_policy", collect_policy),
    path("format_manifest/<path_param>", format_manifest),
    path("archive_manifest", archive_manifest),
    path("publish_schedule", publish_schedule),
    path("compact_cart", compact_cart),
    path("compact_manifest", compact_manifest),
    path("validate_order", validate_order),
]
