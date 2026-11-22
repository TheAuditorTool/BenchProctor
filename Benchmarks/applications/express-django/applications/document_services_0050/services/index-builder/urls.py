from django.http import JsonResponse
from django.urls import path
from search_index import index_document
from summarize_receipt import summarize_receipt
from publish_manifest import publish_manifest
from summarize_ledger import summarize_ledger
from archive_config import archive_config
from audit_window import audit_window
from normalize_profile import normalize_profile


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("index_document", index_document),
    path("summarize_receipt", summarize_receipt),
    path("publish_manifest", publish_manifest),
    path("summarize_ledger", summarize_ledger),
    path("archive_config", archive_config),
    path("audit_window", audit_window),
    path("normalize_profile", normalize_profile),
]
