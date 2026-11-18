from django.http import JsonResponse
from django.urls import path
from config_rollout import rollout_config
from prune_digest import prune_digest
from rotate_batch import rotate_batch
from resolve_config import resolve_config
from resolve_batch import resolve_batch
from verify_checkpoint import verify_checkpoint
from summarize_index import summarize_index
from verify_bundle import verify_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("rollout_config", rollout_config),
    path("prune_digest", prune_digest),
    path("rotate_batch", rotate_batch),
    path("resolve_config", resolve_config),
    path("resolve_batch", resolve_batch),
    path("verify_checkpoint/<path_param>", verify_checkpoint),
    path("summarize_index", summarize_index),
    path("verify_bundle", verify_bundle),
]
