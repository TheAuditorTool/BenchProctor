from django.http import JsonResponse
from django.urls import path
from session_create import create_session
from annotate_snapshot import annotate_snapshot
from compact_digest import compact_digest
from audit_summary import audit_summary
from render_ledger import render_ledger
from format_checkpoint import format_checkpoint
from enrich_session import enrich_session
from enrich_receipt import enrich_receipt


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("create_session", create_session),
    path("annotate_snapshot", annotate_snapshot),
    path("compact_digest", compact_digest),
    path("audit_summary", audit_summary),
    path("render_ledger", render_ledger),
    path("format_checkpoint", format_checkpoint),
    path("enrich_session", enrich_session),
    path("enrich_receipt", enrich_receipt),
]
