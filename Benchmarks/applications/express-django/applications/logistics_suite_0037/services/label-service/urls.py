from django.http import JsonResponse
from django.urls import path
from label_create import create_label
from verify_profile import verify_profile
from prune_label import prune_label
from archive_snapshot import archive_snapshot
from annotate_roster import annotate_roster
from prune_config import prune_config
from compact_waybill import compact_waybill


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("create_label", create_label),
    path("verify_profile", verify_profile),
    path("prune_label", prune_label),
    path("archive_snapshot", archive_snapshot),
    path("annotate_roster", annotate_roster),
    path("prune_config", prune_config),
    path("compact_waybill", compact_waybill),
]
