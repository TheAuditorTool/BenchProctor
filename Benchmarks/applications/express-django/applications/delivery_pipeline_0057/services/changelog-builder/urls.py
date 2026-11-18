from django.http import JsonResponse
from django.urls import path
from changelog_build import build_changelog
from prune_index import prune_index
from collect_digest import collect_digest
from reconcile_schedule import reconcile_schedule
from summarize_receipt import summarize_receipt
from export_checkpoint import export_checkpoint
from resolve_release import resolve_release


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("build_changelog", build_changelog),
    path("prune_index", prune_index),
    path("collect_digest", collect_digest),
    path("reconcile_schedule", reconcile_schedule),
    path("summarize_receipt/<path_param>", summarize_receipt),
    path("export_checkpoint/<path_param>", export_checkpoint),
    path("resolve_release", resolve_release),
]
