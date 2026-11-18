from django.http import JsonResponse
from django.urls import path
from flag_evaluate import evaluate_flag
from render_snapshot import render_snapshot
from normalize_receipt import normalize_receipt
from publish_config import publish_config
from resolve_ledger import resolve_ledger
from merge_window import merge_window
from audit_quota import audit_quota


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("evaluate_flag", evaluate_flag),
    path("render_snapshot", render_snapshot),
    path("normalize_receipt", normalize_receipt),
    path("publish_config", publish_config),
    path("resolve_ledger", resolve_ledger),
    path("merge_window", merge_window),
    path("audit_quota", audit_quota),
]
