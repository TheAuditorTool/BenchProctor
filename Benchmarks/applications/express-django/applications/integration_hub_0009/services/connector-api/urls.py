from django.http import JsonResponse
from django.urls import path
from connector_invoke import invoke_connector
from build_checkpoint import build_checkpoint
from summarize_policy import summarize_policy
from publish_config import publish_config
from collect_bundle import collect_bundle
from summarize_record import summarize_record
from prune_webhook import prune_webhook
from normalize_record import normalize_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("invoke_connector", invoke_connector),
    path("build_checkpoint/<path_param>", build_checkpoint),
    path("summarize_policy", summarize_policy),
    path("publish_config", publish_config),
    path("collect_bundle", collect_bundle),
    path("summarize_record", summarize_record),
    path("prune_webhook", prune_webhook),
    path("normalize_record", normalize_record),
]
