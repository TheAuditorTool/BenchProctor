from django.http import JsonResponse
from django.urls import path
from supplier_feed import pull_supplier_feed
from archive_snapshot import archive_snapshot
from prune_header import prune_header
from validate_window import validate_window
from fetch_ledger import fetch_ledger
from verify_digest import verify_digest
from resolve_snapshot import resolve_snapshot
from format_policy import format_policy


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("pull_supplier_feed", pull_supplier_feed),
    path("archive_snapshot", archive_snapshot),
    path("prune_header", prune_header),
    path("validate_window", validate_window),
    path("fetch_ledger", fetch_ledger),
    path("verify_digest", verify_digest),
    path("resolve_snapshot", resolve_snapshot),
    path("format_policy", format_policy),
]
