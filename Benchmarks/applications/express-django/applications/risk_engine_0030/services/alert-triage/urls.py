from django.http import JsonResponse
from django.urls import path
from alert_triage import triage_alert
from enrich_schedule import enrich_schedule
from compact_roster import compact_roster
from build_decision import build_decision
from reconcile_batch import reconcile_batch
from archive_schedule import archive_schedule
from archive_rule import archive_rule


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("triage_alert", triage_alert),
    path("enrich_schedule", enrich_schedule),
    path("compact_roster", compact_roster),
    path("build_decision", build_decision),
    path("reconcile_batch", reconcile_batch),
    path("archive_schedule", archive_schedule),
    path("archive_rule", archive_rule),
]
