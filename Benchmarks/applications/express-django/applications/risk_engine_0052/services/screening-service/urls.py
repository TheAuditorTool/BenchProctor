from django.http import JsonResponse
from django.urls import path
from screening_run import run_screening
from collect_bundle import collect_bundle
from verify_policy import verify_policy
from validate_policy import validate_policy
from export_batch import export_batch
from resolve_snapshot import resolve_snapshot
from prune_config import prune_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_screening", run_screening),
    path("collect_bundle", collect_bundle),
    path("verify_policy", verify_policy),
    path("validate_policy", validate_policy),
    path("export_batch", export_batch),
    path("resolve_snapshot", resolve_snapshot),
    path("prune_config", prune_config),
]
