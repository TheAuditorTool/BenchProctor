from django.http import JsonResponse
from django.urls import path
from connector_invoke import invoke_connector
from format_digest import format_digest
from archive_connector import archive_connector
from load_batch import load_batch
from collect_digest import collect_digest
from normalize_window import normalize_window
from format_policy import format_policy
from resolve_mapping import resolve_mapping


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("invoke_connector", invoke_connector),
    path("format_digest", format_digest),
    path("archive_connector", archive_connector),
    path("load_batch", load_batch),
    path("collect_digest", collect_digest),
    path("normalize_window", normalize_window),
    path("format_policy", format_policy),
    path("resolve_mapping", resolve_mapping),
]
