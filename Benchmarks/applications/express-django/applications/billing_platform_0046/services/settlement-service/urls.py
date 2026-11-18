from django.http import JsonResponse
from django.urls import path
from settlement_batch import run_settlement
from resolve_snapshot import resolve_snapshot
from compact_receipt import compact_receipt
from rotate_report import rotate_report
from prune_report import prune_report
from validate_schedule import validate_schedule
from fetch_schedule import fetch_schedule


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_settlement", run_settlement),
    path("resolve_snapshot", resolve_snapshot),
    path("compact_receipt", compact_receipt),
    path("rotate_report", rotate_report),
    path("prune_report", prune_report),
    path("validate_schedule", validate_schedule),
    path("fetch_schedule", fetch_schedule),
]
