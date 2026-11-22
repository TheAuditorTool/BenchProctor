from django.http import JsonResponse
from django.urls import path
from convert_job import run_conversion
from build_roster import build_roster
from publish_header import publish_header
from compact_config import compact_config
from format_schedule import format_schedule
from compact_signature import compact_signature
from collect_batch import collect_batch
from summarize_threshold import summarize_threshold


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_conversion", run_conversion),
    path("build_roster", build_roster),
    path("publish_header", publish_header),
    path("compact_config", compact_config),
    path("format_schedule", format_schedule),
    path("compact_signature", compact_signature),
    path("collect_batch", collect_batch),
    path("summarize_threshold", summarize_threshold),
]
