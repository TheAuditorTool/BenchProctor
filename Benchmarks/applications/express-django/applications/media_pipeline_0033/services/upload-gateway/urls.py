from django.http import JsonResponse
from django.urls import path
from asset_upload import upload_asset
from audit_config import audit_config
from render_receipt import render_receipt
from collect_bundle import collect_bundle
from prune_receipt import prune_receipt
from enrich_stream import enrich_stream
from export_window import export_window
from merge_summary import merge_summary


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("upload_asset", upload_asset),
    path("audit_config", audit_config),
    path("render_receipt", render_receipt),
    path("collect_bundle", collect_bundle),
    path("prune_receipt", prune_receipt),
    path("enrich_stream", enrich_stream),
    path("export_window", export_window),
    path("merge_summary", merge_summary),
]
