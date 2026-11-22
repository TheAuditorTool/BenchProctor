from django.http import JsonResponse
from django.urls import path
from watchlist_sync import sync_watchlist
from reconcile_decision import reconcile_decision
from merge_rule import merge_rule
from reconcile_checkpoint import reconcile_checkpoint
from build_ledger import build_ledger
from collect_header import collect_header
from export_rule import export_rule
from fetch_bundle import fetch_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("sync_watchlist", sync_watchlist),
    path("reconcile_decision", reconcile_decision),
    path("merge_rule", merge_rule),
    path("reconcile_checkpoint", reconcile_checkpoint),
    path("build_ledger", build_ledger),
    path("collect_header", collect_header),
    path("export_rule", export_rule),
    path("fetch_bundle", fetch_bundle),
]
