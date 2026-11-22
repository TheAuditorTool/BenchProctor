from django.http import JsonResponse
from django.urls import path
from shipment_quote import quote_shipment
from render_roster import render_roster
from fetch_window import fetch_window
from compact_config import compact_config
from collect_report import collect_report
from collect_ledger import collect_ledger
from normalize_digest import normalize_digest
from build_checkpoint import build_checkpoint


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("quote_shipment", quote_shipment),
    path("render_roster", render_roster),
    path("fetch_window", fetch_window),
    path("compact_config", compact_config),
    path("collect_report", collect_report),
    path("collect_ledger", collect_ledger),
    path("normalize_digest", normalize_digest),
    path("build_checkpoint", build_checkpoint),
]
