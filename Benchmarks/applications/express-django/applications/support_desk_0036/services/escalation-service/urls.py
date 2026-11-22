from django.http import JsonResponse
from django.urls import path
from escalation_raise import raise_escalation
from validate_manifest import validate_manifest
from collect_policy import collect_policy
from resolve_header import resolve_header
from publish_batch import publish_batch
from collect_checkpoint import collect_checkpoint
from enrich_batch import enrich_batch


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("raise_escalation", raise_escalation),
    path("validate_manifest/<path_param>", validate_manifest),
    path("collect_policy", collect_policy),
    path("resolve_header", resolve_header),
    path("publish_batch", publish_batch),
    path("collect_checkpoint", collect_checkpoint),
    path("enrich_batch", enrich_batch),
]
