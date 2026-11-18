from django.http import JsonResponse
from django.urls import path
from queue_bridge import bridge_queue
from rotate_batch import rotate_batch
from validate_roster import validate_roster
from reconcile_manifest import reconcile_manifest
from render_manifest import render_manifest
from resolve_schedule import resolve_schedule
from export_schedule import export_schedule


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("bridge_queue", bridge_queue),
    path("rotate_batch", rotate_batch),
    path("validate_roster", validate_roster),
    path("reconcile_manifest", reconcile_manifest),
    path("render_manifest", render_manifest),
    path("resolve_schedule", resolve_schedule),
    path("export_schedule", export_schedule),
]
