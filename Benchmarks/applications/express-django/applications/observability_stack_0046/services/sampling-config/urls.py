from django.http import JsonResponse
from django.urls import path
from sample_config import configure_sample
from audit_bundle import audit_bundle
from collect_checkpoint import collect_checkpoint
from render_schedule import render_schedule
from load_metric import load_metric
from enrich_roster import enrich_roster
from export_header import export_header


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("configure_sample", configure_sample),
    path("audit_bundle", audit_bundle),
    path("collect_checkpoint", collect_checkpoint),
    path("render_schedule", render_schedule),
    path("load_metric", load_metric),
    path("enrich_roster", enrich_roster),
    path("export_header", export_header),
]
