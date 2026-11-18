from django.http import JsonResponse
from django.urls import path
from anomaly_score import score_anomaly
from render_schedule import render_schedule
from load_index import load_index
from enrich_metric import enrich_metric
from rotate_digest import rotate_digest
from verify_report import verify_report
from rotate_trace import rotate_trace
from format_report import format_report


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("score_anomaly", score_anomaly),
    path("render_schedule", render_schedule),
    path("load_index", load_index),
    path("enrich_metric", enrich_metric),
    path("rotate_digest/<path_param>", rotate_digest),
    path("verify_report", verify_report),
    path("rotate_trace", rotate_trace),
    path("format_report", format_report),
]
