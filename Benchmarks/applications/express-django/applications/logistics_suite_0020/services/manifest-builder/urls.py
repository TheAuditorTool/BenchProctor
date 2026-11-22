from django.http import JsonResponse
from django.urls import path
from manifest_build import build_manifest
from merge_header import merge_header
from verify_threshold import verify_threshold
from normalize_bundle import normalize_bundle
from prune_manifest import prune_manifest
from compact_receipt import compact_receipt
from build_checkpoint import build_checkpoint


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("build_manifest", build_manifest),
    path("merge_header", merge_header),
    path("verify_threshold", verify_threshold),
    path("normalize_bundle", normalize_bundle),
    path("prune_manifest", prune_manifest),
    path("compact_receipt", compact_receipt),
    path("build_checkpoint", build_checkpoint),
]
