from django.http import JsonResponse
from django.urls import path
from alert_route import route_alert
from audit_digest import audit_digest
from rotate_checkpoint import rotate_checkpoint
from compact_receipt import compact_receipt
from reconcile_sample import reconcile_sample
from export_schedule import export_schedule
from build_snapshot import build_snapshot


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("route_alert", route_alert),
    path("audit_digest", audit_digest),
    path("rotate_checkpoint", rotate_checkpoint),
    path("compact_receipt", compact_receipt),
    path("reconcile_sample", reconcile_sample),
    path("export_schedule", export_schedule),
    path("build_snapshot", build_snapshot),
]
