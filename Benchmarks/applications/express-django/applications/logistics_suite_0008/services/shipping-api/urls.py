from django.http import JsonResponse
from django.urls import path
from shipment_quote import quote_shipment
from publish_ledger import publish_ledger
from verify_threshold import verify_threshold
from fetch_policy import fetch_policy
from format_report import format_report
from merge_batch import merge_batch
from build_snapshot import build_snapshot


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("quote_shipment", quote_shipment),
    path("publish_ledger", publish_ledger),
    path("verify_threshold", verify_threshold),
    path("fetch_policy", fetch_policy),
    path("format_report", format_report),
    path("merge_batch", merge_batch),
    path("build_snapshot", build_snapshot),
]
