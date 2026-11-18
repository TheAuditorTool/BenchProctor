from django.http import JsonResponse
from django.urls import path
from directory_sync import sync_directory
from prune_ledger import prune_ledger
from rotate_manifest import rotate_manifest
from format_threshold import format_threshold
from validate_manifest import validate_manifest
from fetch_policy import fetch_policy
from normalize_config import normalize_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("sync_directory", sync_directory),
    path("prune_ledger", prune_ledger),
    path("rotate_manifest", rotate_manifest),
    path("format_threshold", format_threshold),
    path("validate_manifest", validate_manifest),
    path("fetch_policy", fetch_policy),
    path("normalize_config", normalize_config),
]
