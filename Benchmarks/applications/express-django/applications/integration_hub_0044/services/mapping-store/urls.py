from django.http import JsonResponse
from django.urls import path
from field_mapping import map_field
from fetch_record import fetch_record
from fetch_ledger import fetch_ledger
from format_roster import format_roster
from collect_connector import collect_connector
from publish_summary import publish_summary
from archive_mapping import archive_mapping


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("map_field", map_field),
    path("fetch_record", fetch_record),
    path("fetch_ledger", fetch_ledger),
    path("format_roster", format_roster),
    path("collect_connector", collect_connector),
    path("publish_summary", publish_summary),
    path("archive_mapping", archive_mapping),
]
