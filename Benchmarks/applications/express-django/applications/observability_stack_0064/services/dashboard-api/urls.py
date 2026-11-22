from django.http import JsonResponse
from django.urls import path
from dashboard_query import query_dashboard
from validate_profile import validate_profile
from enrich_report import enrich_report
from annotate_receipt import annotate_receipt
from fetch_snapshot import fetch_snapshot
from summarize_window import summarize_window
from fetch_sample import fetch_sample


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("query_dashboard", query_dashboard),
    path("validate_profile", validate_profile),
    path("enrich_report", enrich_report),
    path("annotate_receipt", annotate_receipt),
    path("fetch_snapshot", fetch_snapshot),
    path("summarize_window", summarize_window),
    path("fetch_sample", fetch_sample),
]
