from django.http import JsonResponse
from django.urls import path
from metric_ingest import ingest_metric
from summarize_trace import summarize_trace
from format_header import format_header
from normalize_config import normalize_config
from summarize_digest import summarize_digest
from publish_checkpoint import publish_checkpoint
from export_digest import export_digest
from normalize_index import normalize_index


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("ingest_metric", ingest_metric),
    path("summarize_trace", summarize_trace),
    path("format_header", format_header),
    path("normalize_config", normalize_config),
    path("summarize_digest", summarize_digest),
    path("publish_checkpoint", publish_checkpoint),
    path("export_digest/<path_param>", export_digest),
    path("normalize_index", normalize_index),
]
