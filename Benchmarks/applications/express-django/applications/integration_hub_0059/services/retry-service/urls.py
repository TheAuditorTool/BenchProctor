from django.http import JsonResponse
from django.urls import path
from retry_queue import queue_retry
from render_window import render_window
from enrich_mapping import enrich_mapping
from collect_manifest import collect_manifest
from collect_checkpoint import collect_checkpoint
from audit_roster import audit_roster
from export_digest import export_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("queue_retry", queue_retry),
    path("render_window", render_window),
    path("enrich_mapping", enrich_mapping),
    path("collect_manifest", collect_manifest),
    path("collect_checkpoint", collect_checkpoint),
    path("audit_roster", audit_roster),
    path("export_digest", export_digest),
]
