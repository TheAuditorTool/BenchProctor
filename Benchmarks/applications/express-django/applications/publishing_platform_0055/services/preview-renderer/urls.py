from django.http import JsonResponse
from django.urls import path
from preview_render import render_preview
from enrich_bundle import enrich_bundle
from validate_policy import validate_policy
from format_bundle import format_bundle
from render_threshold import render_threshold
from build_bundle import build_bundle
from summarize_config import summarize_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("render_preview", render_preview),
    path("enrich_bundle", enrich_bundle),
    path("validate_policy", validate_policy),
    path("format_bundle", format_bundle),
    path("render_threshold", render_threshold),
    path("build_bundle", build_bundle),
    path("summarize_config", summarize_config),
]
