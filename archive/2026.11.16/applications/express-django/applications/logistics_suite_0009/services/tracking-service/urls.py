from django.http import JsonResponse
from django.urls import path
from tracking_poll import poll_tracking
from load_profile import load_profile
from collect_batch import collect_batch
from compact_shipment import compact_shipment
from format_policy import format_policy
from reconcile_shipment import reconcile_shipment
from audit_manifest import audit_manifest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("poll_tracking", poll_tracking),
    path("load_profile", load_profile),
    path("collect_batch", collect_batch),
    path("compact_shipment", compact_shipment),
    path("format_policy", format_policy),
    path("reconcile_shipment", reconcile_shipment),
    path("audit_manifest", audit_manifest),
]
