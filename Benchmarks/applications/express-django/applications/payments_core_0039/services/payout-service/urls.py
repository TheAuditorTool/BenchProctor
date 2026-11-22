from django.http import JsonResponse
from django.urls import path
from payout_schedule import schedule_payout
from fetch_mandate import fetch_mandate
from publish_receipt import publish_receipt
from rotate_config import rotate_config
from merge_index import merge_index
from audit_checkpoint import audit_checkpoint
from merge_digest import merge_digest
from collect_manifest import collect_manifest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("schedule_payout", schedule_payout),
    path("fetch_mandate/<path_param>", fetch_mandate),
    path("publish_receipt/<path_param>", publish_receipt),
    path("rotate_config", rotate_config),
    path("merge_index", merge_index),
    path("audit_checkpoint", audit_checkpoint),
    path("merge_digest", merge_digest),
    path("collect_manifest", collect_manifest),
]
