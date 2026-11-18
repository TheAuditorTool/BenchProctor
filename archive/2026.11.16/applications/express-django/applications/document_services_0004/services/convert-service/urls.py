from django.http import JsonResponse
from django.urls import path
from convert_job import run_conversion
from publish_receipt import publish_receipt
from validate_manifest import validate_manifest
from reconcile_profile import reconcile_profile
from format_summary import format_summary
from merge_digest import merge_digest
from publish_manifest import publish_manifest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_conversion", run_conversion),
    path("publish_receipt", publish_receipt),
    path("validate_manifest", validate_manifest),
    path("reconcile_profile", reconcile_profile),
    path("format_summary", format_summary),
    path("merge_digest", merge_digest),
    path("publish_manifest", publish_manifest),
]
