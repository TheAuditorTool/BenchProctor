from django.http import JsonResponse
from django.urls import path
from promo_apply import apply_promo
from merge_manifest import merge_manifest
from merge_profile import merge_profile
from resolve_cart import resolve_cart
from prune_promotion import prune_promotion
from collect_threshold import collect_threshold
from archive_policy import archive_policy


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("apply_promo", apply_promo),
    path("merge_manifest", merge_manifest),
    path("merge_profile", merge_profile),
    path("resolve_cart", resolve_cart),
    path("prune_promotion", prune_promotion),
    path("collect_threshold", collect_threshold),
    path("archive_policy", archive_policy),
]
