from django.http import JsonResponse
from django.urls import path
from service_register import register_service
from resolve_index import resolve_index
from normalize_roster import normalize_roster
from archive_batch import archive_batch
from collect_receipt import collect_receipt
from compact_bundle import compact_bundle
from collect_manifest import collect_manifest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("register_service", register_service),
    path("resolve_index", resolve_index),
    path("normalize_roster", normalize_roster),
    path("archive_batch", archive_batch),
    path("collect_receipt", collect_receipt),
    path("compact_bundle", compact_bundle),
    path("collect_manifest", collect_manifest),
]
