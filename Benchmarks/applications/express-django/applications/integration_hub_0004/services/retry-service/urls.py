from django.http import JsonResponse
from django.urls import path
from retry_queue import queue_retry
from publish_summary import publish_summary
from audit_ledger import audit_ledger
from merge_config import merge_config
from prune_partner import prune_partner
from validate_connector import validate_connector
from normalize_checkpoint import normalize_checkpoint


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("queue_retry", queue_retry),
    path("publish_summary", publish_summary),
    path("audit_ledger", audit_ledger),
    path("merge_config", merge_config),
    path("prune_partner", prune_partner),
    path("validate_connector", validate_connector),
    path("normalize_checkpoint", normalize_checkpoint),
]
