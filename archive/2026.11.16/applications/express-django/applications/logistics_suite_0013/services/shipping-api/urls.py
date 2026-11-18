from django.http import JsonResponse
from django.urls import path
from shipment_quote import quote_shipment
from compact_window import compact_window
from enrich_checkpoint import enrich_checkpoint
from reconcile_snapshot import reconcile_snapshot
from export_summary import export_summary
from enrich_report import enrich_report
from load_index import load_index


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("quote_shipment", quote_shipment),
    path("compact_window", compact_window),
    path("enrich_checkpoint", enrich_checkpoint),
    path("reconcile_snapshot", reconcile_snapshot),
    path("export_summary", export_summary),
    path("enrich_report", enrich_report),
    path("load_index", load_index),
]
