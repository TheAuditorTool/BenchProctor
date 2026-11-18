from django.http import JsonResponse
from django.urls import path
from shipment_quote import quote_shipment
from render_threshold import render_threshold
from export_index import export_index
from fetch_batch import fetch_batch
from merge_snapshot import merge_snapshot
from reconcile_roster import reconcile_roster
from normalize_batch import normalize_batch


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("quote_shipment", quote_shipment),
    path("render_threshold", render_threshold),
    path("export_index/<path_param>", export_index),
    path("fetch_batch", fetch_batch),
    path("merge_snapshot", merge_snapshot),
    path("reconcile_roster", reconcile_roster),
    path("normalize_batch", normalize_batch),
]
