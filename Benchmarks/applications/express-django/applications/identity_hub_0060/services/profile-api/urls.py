from django.http import JsonResponse
from django.urls import path
from profile_update import update_profile
from format_snapshot import format_snapshot
from build_report import build_report
from audit_device import audit_device
from merge_receipt import merge_receipt
from verify_window import verify_window
from normalize_profile import normalize_profile


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("update_profile", update_profile),
    path("format_snapshot", format_snapshot),
    path("build_report", build_report),
    path("audit_device", audit_device),
    path("merge_receipt", merge_receipt),
    path("verify_window", verify_window),
    path("normalize_profile", normalize_profile),
]
