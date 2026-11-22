from django.http import JsonResponse
from django.urls import path
from session_create import create_session
from render_config import render_config
from archive_ledger import archive_ledger
from normalize_threshold import normalize_threshold
from reconcile_roster import reconcile_roster
from annotate_device import annotate_device
from summarize_batch import summarize_batch


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("create_session", create_session),
    path("render_config", render_config),
    path("archive_ledger", archive_ledger),
    path("normalize_threshold", normalize_threshold),
    path("reconcile_roster", reconcile_roster),
    path("annotate_device", annotate_device),
    path("summarize_batch", summarize_batch),
]
