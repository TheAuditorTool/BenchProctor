from django.http import JsonResponse
from django.urls import path
from transcode_job import enqueue_transcode
from enrich_threshold import enrich_threshold
from reconcile_asset import reconcile_asset
from verify_receipt import verify_receipt
from enrich_receipt import enrich_receipt
from publish_profile import publish_profile
from prune_rendition import prune_rendition


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("enqueue_transcode", enqueue_transcode),
    path("enrich_threshold", enrich_threshold),
    path("reconcile_asset", reconcile_asset),
    path("verify_receipt", verify_receipt),
    path("enrich_receipt", enrich_receipt),
    path("publish_profile", publish_profile),
    path("prune_rendition", prune_rendition),
]
