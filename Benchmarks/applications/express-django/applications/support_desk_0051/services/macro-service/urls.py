from django.http import JsonResponse
from django.urls import path
from macro_apply import apply_macro
from audit_threshold import audit_threshold
from archive_survey import archive_survey
from export_manifest import export_manifest
from merge_window import merge_window
from load_receipt import load_receipt
from resolve_window import resolve_window


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("apply_macro", apply_macro),
    path("audit_threshold", audit_threshold),
    path("archive_survey", archive_survey),
    path("export_manifest", export_manifest),
    path("merge_window", merge_window),
    path("load_receipt", load_receipt),
    path("resolve_window", resolve_window),
]
