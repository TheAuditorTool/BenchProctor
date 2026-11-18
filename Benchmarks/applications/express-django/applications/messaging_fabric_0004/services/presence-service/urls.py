from django.http import JsonResponse
from django.urls import path
from presence_update import update_presence
from enrich_summary import enrich_summary
from load_receipt import load_receipt
from enrich_receipt import enrich_receipt
from validate_report import validate_report
from export_config import export_config
from annotate_snapshot import annotate_snapshot


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("update_presence", update_presence),
    path("enrich_summary", enrich_summary),
    path("load_receipt", load_receipt),
    path("enrich_receipt", enrich_receipt),
    path("validate_report", validate_report),
    path("export_config", export_config),
    path("annotate_snapshot", annotate_snapshot),
]
