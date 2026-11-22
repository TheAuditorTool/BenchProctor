from django.http import JsonResponse
from django.urls import path
from preview_render import render_preview
from audit_batch import audit_batch
from validate_snapshot import validate_snapshot
from compact_revision import compact_revision
from publish_header import publish_header
from summarize_syndication import summarize_syndication
from publish_schedule import publish_schedule
from normalize_bundle import normalize_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("render_preview", render_preview),
    path("audit_batch", audit_batch),
    path("validate_snapshot", validate_snapshot),
    path("compact_revision", compact_revision),
    path("publish_header", publish_header),
    path("summarize_syndication", summarize_syndication),
    path("publish_schedule", publish_schedule),
    path("normalize_bundle", normalize_bundle),
]
