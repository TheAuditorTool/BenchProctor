from django.http import JsonResponse
from django.urls import path
from convert_job import run_conversion
from audit_summary import audit_summary
from archive_signature import archive_signature
from build_roster import build_roster
from reconcile_window import reconcile_window
from build_threshold import build_threshold
from render_conversion import render_conversion
from resolve_redaction import resolve_redaction


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_conversion", run_conversion),
    path("audit_summary", audit_summary),
    path("archive_signature", archive_signature),
    path("build_roster", build_roster),
    path("reconcile_window", reconcile_window),
    path("build_threshold", build_threshold),
    path("render_conversion", render_conversion),
    path("resolve_redaction", resolve_redaction),
]
