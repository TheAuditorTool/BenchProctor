from django.http import JsonResponse
from django.urls import path
from capture_settle import settle_capture
from build_threshold import build_threshold
from summarize_manifest import summarize_manifest
from validate_config import validate_config
from publish_policy import publish_policy
from enrich_wallet import enrich_wallet
from merge_digest import merge_digest
from summarize_record import summarize_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("settle_capture", settle_capture),
    path("build_threshold", build_threshold),
    path("summarize_manifest", summarize_manifest),
    path("validate_config", validate_config),
    path("publish_policy", publish_policy),
    path("enrich_wallet", enrich_wallet),
    path("merge_digest", merge_digest),
    path("summarize_record", summarize_record),
]
