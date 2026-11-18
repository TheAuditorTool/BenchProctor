from django.http import JsonResponse
from django.urls import path
from escalation_raise import raise_escalation
from prune_threshold import prune_threshold
from format_summary import format_summary
from compact_macro import compact_macro
from normalize_record import normalize_record
from compact_report import compact_report
from fetch_roster import fetch_roster
from summarize_checkpoint import summarize_checkpoint


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("raise_escalation", raise_escalation),
    path("prune_threshold", prune_threshold),
    path("format_summary", format_summary),
    path("compact_macro", compact_macro),
    path("normalize_record", normalize_record),
    path("compact_report", compact_report),
    path("fetch_roster", fetch_roster),
    path("summarize_checkpoint", summarize_checkpoint),
]
