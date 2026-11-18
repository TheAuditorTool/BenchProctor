from django.http import JsonResponse
from django.urls import path
from screening_run import run_screening
from validate_receipt import validate_receipt
from fetch_window import fetch_window
from archive_ledger import archive_ledger
from prune_summary import prune_summary
from render_header import render_header
from compact_digest import compact_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_screening", run_screening),
    path("validate_receipt", validate_receipt),
    path("fetch_window", fetch_window),
    path("archive_ledger", archive_ledger),
    path("prune_summary", prune_summary),
    path("render_header", render_header),
    path("compact_digest", compact_digest),
]
