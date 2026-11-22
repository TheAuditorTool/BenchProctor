from django.http import JsonResponse
from django.urls import path
from sample_config import configure_sample
from summarize_schedule import summarize_schedule
from merge_digest import merge_digest
from archive_manifest import archive_manifest
from prune_record import prune_record
from compact_metric import compact_metric
from format_roster import format_roster


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("configure_sample", configure_sample),
    path("summarize_schedule", summarize_schedule),
    path("merge_digest", merge_digest),
    path("archive_manifest", archive_manifest),
    path("prune_record", prune_record),
    path("compact_metric", compact_metric),
    path("format_roster", format_roster),
]
