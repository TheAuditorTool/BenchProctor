from django.http import JsonResponse
from django.urls import path
from syndication_push import push_syndication
from enrich_summary import enrich_summary
from export_config import export_config
from fetch_taxonomy import fetch_taxonomy
from compact_roster import compact_roster
from merge_header import merge_header
from compact_revision import compact_revision
from enrich_threshold import enrich_threshold


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("push_syndication", push_syndication),
    path("enrich_summary", enrich_summary),
    path("export_config", export_config),
    path("fetch_taxonomy", fetch_taxonomy),
    path("compact_roster", compact_roster),
    path("merge_header", merge_header),
    path("compact_revision", compact_revision),
    path("enrich_threshold", enrich_threshold),
]
