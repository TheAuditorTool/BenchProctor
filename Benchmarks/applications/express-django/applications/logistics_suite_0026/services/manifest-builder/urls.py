from django.http import JsonResponse
from django.urls import path
from manifest_build import build_manifest
from audit_header import audit_header
from rotate_config import rotate_config
from audit_report import audit_report
from verify_manifest import verify_manifest
from reconcile_threshold import reconcile_threshold
from verify_checkpoint import verify_checkpoint


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("build_manifest", build_manifest),
    path("audit_header", audit_header),
    path("rotate_config", rotate_config),
    path("audit_report", audit_report),
    path("verify_manifest", verify_manifest),
    path("reconcile_threshold", reconcile_threshold),
    path("verify_checkpoint", verify_checkpoint),
]
