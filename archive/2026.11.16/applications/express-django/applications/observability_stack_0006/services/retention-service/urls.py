from django.http import JsonResponse
from django.urls import path
from retention_sweep import sweep_retention
from publish_sample import publish_sample
from annotate_schedule import annotate_schedule
from prune_metric import prune_metric
from normalize_manifest import normalize_manifest
from rotate_ledger import rotate_ledger
from load_manifest import load_manifest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("sweep_retention", sweep_retention),
    path("publish_sample", publish_sample),
    path("annotate_schedule", annotate_schedule),
    path("prune_metric", prune_metric),
    path("normalize_manifest", normalize_manifest),
    path("rotate_ledger", rotate_ledger),
    path("load_manifest", load_manifest),
]
