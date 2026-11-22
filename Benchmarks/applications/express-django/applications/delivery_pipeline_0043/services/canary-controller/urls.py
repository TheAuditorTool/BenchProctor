from django.http import JsonResponse
from django.urls import path
from canary_promote import promote_canary
from collect_threshold import collect_threshold
from prune_window import prune_window
from verify_report import verify_report
from publish_record import publish_record
from build_receipt import build_receipt
from rotate_policy import rotate_policy


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("promote_canary", promote_canary),
    path("collect_threshold/<path_param>", collect_threshold),
    path("prune_window", prune_window),
    path("verify_report", verify_report),
    path("publish_record", publish_record),
    path("build_receipt", build_receipt),
    path("rotate_policy", rotate_policy),
]
