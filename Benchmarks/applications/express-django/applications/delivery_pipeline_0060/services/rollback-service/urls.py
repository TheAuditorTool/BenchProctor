from django.http import JsonResponse
from django.urls import path
from rollback_trigger import trigger_rollback
from load_roster import load_roster
from summarize_release import summarize_release
from verify_receipt import verify_receipt
from export_artifact import export_artifact
from verify_checkpoint import verify_checkpoint
from fetch_roster import fetch_roster


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("trigger_rollback", trigger_rollback),
    path("load_roster", load_roster),
    path("summarize_release", summarize_release),
    path("verify_receipt", verify_receipt),
    path("export_artifact", export_artifact),
    path("verify_checkpoint", verify_checkpoint),
    path("fetch_roster", fetch_roster),
]
