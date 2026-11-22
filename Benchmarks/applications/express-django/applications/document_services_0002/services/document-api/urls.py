from django.http import JsonResponse
from django.urls import path
from document_upload import upload_document
from audit_batch import audit_batch
from load_receipt import load_receipt
from reconcile_threshold import reconcile_threshold
from audit_record import audit_record
from enrich_manifest import enrich_manifest
from build_signature import build_signature


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("upload_document", upload_document),
    path("audit_batch", audit_batch),
    path("load_receipt", load_receipt),
    path("reconcile_threshold", reconcile_threshold),
    path("audit_record", audit_record),
    path("enrich_manifest", enrich_manifest),
    path("build_signature", build_signature),
]
