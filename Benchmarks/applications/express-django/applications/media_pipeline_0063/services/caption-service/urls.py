from django.http import JsonResponse
from django.urls import path
from caption_extract import extract_caption
from publish_report import publish_report
from enrich_ledger import enrich_ledger
from format_asset import format_asset
from build_index import build_index
from audit_receipt import audit_receipt
from annotate_manifest import annotate_manifest
from validate_receipt import validate_receipt


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("extract_caption", extract_caption),
    path("publish_report", publish_report),
    path("enrich_ledger", enrich_ledger),
    path("format_asset", format_asset),
    path("build_index", build_index),
    path("audit_receipt", audit_receipt),
    path("annotate_manifest", annotate_manifest),
    path("validate_receipt", validate_receipt),
]
