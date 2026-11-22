from django.http import JsonResponse
from django.urls import path
from convert_job import run_conversion
from render_snapshot import render_snapshot
from compact_roster import compact_roster
from render_conversion import render_conversion
from collect_snapshot import collect_snapshot
from archive_bundle import archive_bundle
from build_manifest import build_manifest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_conversion", run_conversion),
    path("render_snapshot", render_snapshot),
    path("compact_roster", compact_roster),
    path("render_conversion", render_conversion),
    path("collect_snapshot", collect_snapshot),
    path("archive_bundle", archive_bundle),
    path("build_manifest", build_manifest),
]
