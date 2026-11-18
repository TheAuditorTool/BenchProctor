from django.http import JsonResponse
from django.urls import path
from rate_shop import shop_rate
from enrich_checkpoint import enrich_checkpoint
from audit_threshold import audit_threshold
from annotate_threshold import annotate_threshold
from collect_index import collect_index
from merge_ledger import merge_ledger
from rotate_manifest import rotate_manifest
from publish_manifest import publish_manifest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("shop_rate", shop_rate),
    path("enrich_checkpoint/<path_param>", enrich_checkpoint),
    path("audit_threshold", audit_threshold),
    path("annotate_threshold", annotate_threshold),
    path("collect_index", collect_index),
    path("merge_ledger", merge_ledger),
    path("rotate_manifest", rotate_manifest),
    path("publish_manifest", publish_manifest),
]
