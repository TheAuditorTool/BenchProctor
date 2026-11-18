from django.http import JsonResponse
from django.urls import path
from ocr_extract import extract_text
from publish_checkpoint import publish_checkpoint
from annotate_schedule import annotate_schedule
from compact_header import compact_header
from render_conversion import render_conversion
from render_attachment import render_attachment
from normalize_config import normalize_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("extract_text", extract_text),
    path("publish_checkpoint", publish_checkpoint),
    path("annotate_schedule", annotate_schedule),
    path("compact_header", compact_header),
    path("render_conversion", render_conversion),
    path("render_attachment", render_attachment),
    path("normalize_config/<path_param>", normalize_config),
]
