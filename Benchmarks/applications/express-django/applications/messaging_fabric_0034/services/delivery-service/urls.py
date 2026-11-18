from django.http import JsonResponse
from django.urls import path
from delivery_dispatch import dispatch_delivery
from normalize_schedule import normalize_schedule
from resolve_checkpoint import resolve_checkpoint
from publish_summary import publish_summary
from archive_checkpoint import archive_checkpoint
from normalize_receipt import normalize_receipt
from normalize_config import normalize_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("dispatch_delivery", dispatch_delivery),
    path("normalize_schedule", normalize_schedule),
    path("resolve_checkpoint", resolve_checkpoint),
    path("publish_summary", publish_summary),
    path("archive_checkpoint", archive_checkpoint),
    path("normalize_receipt", normalize_receipt),
    path("normalize_config", normalize_config),
]
