from django.http import JsonResponse
from django.urls import path
from syndication_push import push_syndication
from annotate_index import annotate_index
from prune_syndication import prune_syndication
from reconcile_window import reconcile_window
from summarize_config import summarize_config
from format_checkpoint import format_checkpoint
from fetch_summary import fetch_summary


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("push_syndication", push_syndication),
    path("annotate_index", annotate_index),
    path("prune_syndication", prune_syndication),
    path("reconcile_window", reconcile_window),
    path("summarize_config", summarize_config),
    path("format_checkpoint", format_checkpoint),
    path("fetch_summary", fetch_summary),
]
