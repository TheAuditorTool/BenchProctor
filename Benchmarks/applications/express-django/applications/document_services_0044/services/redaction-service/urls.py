from django.http import JsonResponse
from django.urls import path
from redaction_apply import apply_redaction
from rotate_bundle import rotate_bundle
from publish_threshold import publish_threshold
from normalize_report import normalize_report
from verify_snapshot import verify_snapshot
from validate_index import validate_index
from reconcile_threshold import reconcile_threshold


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("apply_redaction", apply_redaction),
    path("rotate_bundle", rotate_bundle),
    path("publish_threshold", publish_threshold),
    path("normalize_report", normalize_report),
    path("verify_snapshot", verify_snapshot),
    path("validate_index", validate_index),
    path("reconcile_threshold", reconcile_threshold),
]
