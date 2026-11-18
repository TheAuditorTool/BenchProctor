from django.http import JsonResponse
from django.urls import path
from connector_invoke import invoke_connector
from validate_webhook import validate_webhook
from format_header import format_header
from reconcile_snapshot import reconcile_snapshot
from export_window import export_window
from export_policy import export_policy
from summarize_batch import summarize_batch
from render_config import render_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("invoke_connector", invoke_connector),
    path("validate_webhook", validate_webhook),
    path("format_header/<path_param>", format_header),
    path("reconcile_snapshot", reconcile_snapshot),
    path("export_window", export_window),
    path("export_policy", export_policy),
    path("summarize_batch/<path_param>", summarize_batch),
    path("render_config", render_config),
]
