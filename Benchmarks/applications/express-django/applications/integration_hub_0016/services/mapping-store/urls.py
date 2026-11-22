from django.http import JsonResponse
from django.urls import path
from field_mapping import map_field
from format_mapping import format_mapping
from merge_manifest import merge_manifest
from publish_connector import publish_connector
from prune_index import prune_index
from validate_snapshot import validate_snapshot
from export_record import export_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("map_field", map_field),
    path("format_mapping", format_mapping),
    path("merge_manifest", merge_manifest),
    path("publish_connector", publish_connector),
    path("prune_index", prune_index),
    path("validate_snapshot", validate_snapshot),
    path("export_record", export_record),
]
