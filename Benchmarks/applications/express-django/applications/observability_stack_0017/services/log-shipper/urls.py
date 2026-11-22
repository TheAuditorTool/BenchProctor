from django.http import JsonResponse
from django.urls import path
from log_ship import ship_log
from resolve_ledger import resolve_ledger
from normalize_policy import normalize_policy
from resolve_snapshot import resolve_snapshot
from load_record import load_record
from compact_config import compact_config
from render_policy import render_policy
from reconcile_header import reconcile_header


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("ship_log", ship_log),
    path("resolve_ledger", resolve_ledger),
    path("normalize_policy", normalize_policy),
    path("resolve_snapshot", resolve_snapshot),
    path("load_record", load_record),
    path("compact_config", compact_config),
    path("render_policy", render_policy),
    path("reconcile_header", reconcile_header),
]
