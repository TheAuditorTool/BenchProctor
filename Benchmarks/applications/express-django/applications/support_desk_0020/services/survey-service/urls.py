from django.http import JsonResponse
from django.urls import path
from survey_send import send_survey
from render_ticket import render_ticket
from load_bundle import load_bundle
from archive_config import archive_config
from archive_snapshot import archive_snapshot
from validate_window import validate_window
from validate_bundle import validate_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("send_survey", send_survey),
    path("render_ticket", render_ticket),
    path("load_bundle", load_bundle),
    path("archive_config", archive_config),
    path("archive_snapshot", archive_snapshot),
    path("validate_window", validate_window),
    path("validate_bundle", validate_bundle),
]
