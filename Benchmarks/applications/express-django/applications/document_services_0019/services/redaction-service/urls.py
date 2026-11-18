from django.http import JsonResponse
from django.urls import path
from redaction_apply import apply_redaction
from compact_index import compact_index
from compact_digest import compact_digest
from publish_summary import publish_summary
from reconcile_index import reconcile_index
from summarize_record import summarize_record
from fetch_config import fetch_config
from fetch_index import fetch_index


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("apply_redaction", apply_redaction),
    path("compact_index", compact_index),
    path("compact_digest/<path_param>", compact_digest),
    path("publish_summary", publish_summary),
    path("reconcile_index", reconcile_index),
    path("summarize_record", summarize_record),
    path("fetch_config", fetch_config),
    path("fetch_index", fetch_index),
]
