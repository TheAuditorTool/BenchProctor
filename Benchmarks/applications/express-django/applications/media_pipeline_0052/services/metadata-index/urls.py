from django.http import JsonResponse
from django.urls import path
from metadata_index import index_metadata
from reconcile_record import reconcile_record
from fetch_receipt import fetch_receipt
from format_report import format_report
from fetch_batch import fetch_batch
from format_policy import format_policy
from validate_bundle import validate_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("index_metadata", index_metadata),
    path("reconcile_record", reconcile_record),
    path("fetch_receipt", fetch_receipt),
    path("format_report", format_report),
    path("fetch_batch", fetch_batch),
    path("format_policy", format_policy),
    path("validate_bundle", validate_bundle),
]
