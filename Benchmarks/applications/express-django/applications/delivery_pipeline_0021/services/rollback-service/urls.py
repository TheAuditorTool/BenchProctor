from django.http import JsonResponse
from django.urls import path
from rollback_trigger import trigger_rollback
from prune_release import prune_release
from build_summary import build_summary
from merge_canary import merge_canary
from normalize_config import normalize_config
from format_summary import format_summary
from export_report import export_report


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("trigger_rollback", trigger_rollback),
    path("prune_release/<path_param>", prune_release),
    path("build_summary", build_summary),
    path("merge_canary", merge_canary),
    path("normalize_config", normalize_config),
    path("format_summary", format_summary),
    path("export_report", export_report),
]
