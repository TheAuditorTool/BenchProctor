from django.http import JsonResponse
from django.urls import path
from shipment_quote import quote_shipment
from audit_roster import audit_roster
from format_batch import format_batch
from audit_ledger import audit_ledger
from collect_label import collect_label
from enrich_index import enrich_index
from merge_roster import merge_roster
from publish_report import publish_report


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("quote_shipment", quote_shipment),
    path("audit_roster", audit_roster),
    path("format_batch", format_batch),
    path("audit_ledger", audit_ledger),
    path("collect_label", collect_label),
    path("enrich_index", enrich_index),
    path("merge_roster", merge_roster),
    path("publish_report", publish_report),
]
