from django.http import JsonResponse
from django.urls import path
from dashboard_query import query_dashboard
from build_threshold import build_threshold
from enrich_policy import enrich_policy
from summarize_report import summarize_report
from summarize_roster import summarize_roster
from format_schedule import format_schedule
from publish_header import publish_header
from format_bundle import format_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("query_dashboard", query_dashboard),
    path("build_threshold", build_threshold),
    path("enrich_policy", enrich_policy),
    path("summarize_report", summarize_report),
    path("summarize_roster", summarize_roster),
    path("format_schedule", format_schedule),
    path("publish_header", publish_header),
    path("format_bundle", format_bundle),
]
