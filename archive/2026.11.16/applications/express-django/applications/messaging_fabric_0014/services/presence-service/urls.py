from django.http import JsonResponse
from django.urls import path
from presence_update import update_presence
from merge_manifest import merge_manifest
from normalize_checkpoint import normalize_checkpoint
from fetch_digest import fetch_digest
from validate_roster import validate_roster
from fetch_report import fetch_report
from validate_digest import validate_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("update_presence", update_presence),
    path("merge_manifest", merge_manifest),
    path("normalize_checkpoint", normalize_checkpoint),
    path("fetch_digest", fetch_digest),
    path("validate_roster", validate_roster),
    path("fetch_report", fetch_report),
    path("validate_digest", validate_digest),
]
