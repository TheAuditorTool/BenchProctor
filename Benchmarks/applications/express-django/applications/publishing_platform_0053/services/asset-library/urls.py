from django.http import JsonResponse
from django.urls import path
from asset_attach import attach_asset
from export_article import export_article
from summarize_summary import summarize_summary
from summarize_revision import summarize_revision
from enrich_schedule import enrich_schedule
from merge_revision import merge_revision
from format_index import format_index
from fetch_config import fetch_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("attach_asset", attach_asset),
    path("export_article", export_article),
    path("summarize_summary", summarize_summary),
    path("summarize_revision", summarize_revision),
    path("enrich_schedule", enrich_schedule),
    path("merge_revision", merge_revision),
    path("format_index", format_index),
    path("fetch_config", fetch_config),
]
