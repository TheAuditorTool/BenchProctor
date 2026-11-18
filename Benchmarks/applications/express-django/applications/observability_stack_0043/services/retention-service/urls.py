from django.http import JsonResponse
from django.urls import path
from retention_sweep import sweep_retention
from summarize_alert import summarize_alert
from audit_manifest import audit_manifest
from prune_alert import prune_alert
from load_manifest import load_manifest
from render_threshold import render_threshold
from fetch_window import fetch_window
from prune_config import prune_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("sweep_retention", sweep_retention),
    path("summarize_alert", summarize_alert),
    path("audit_manifest", audit_manifest),
    path("prune_alert/<path_param>", prune_alert),
    path("load_manifest", load_manifest),
    path("render_threshold", render_threshold),
    path("fetch_window", fetch_window),
    path("prune_config", prune_config),
]
