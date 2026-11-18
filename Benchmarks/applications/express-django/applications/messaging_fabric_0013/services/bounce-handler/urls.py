from django.http import JsonResponse
from django.urls import path
from bounce_record import record_bounce
from compact_ledger import compact_ledger
from render_report import render_report
from enrich_header import enrich_header
from format_checkpoint import format_checkpoint
from publish_schedule import publish_schedule
from summarize_schedule import summarize_schedule
from audit_message import audit_message


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("record_bounce", record_bounce),
    path("compact_ledger", compact_ledger),
    path("render_report", render_report),
    path("enrich_header", enrich_header),
    path("format_checkpoint", format_checkpoint),
    path("publish_schedule", publish_schedule),
    path("summarize_schedule", summarize_schedule),
    path("audit_message", audit_message),
]
