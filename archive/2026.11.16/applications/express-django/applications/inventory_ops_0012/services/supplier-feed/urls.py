from django.http import JsonResponse
from django.urls import path
from supplier_feed import pull_supplier_feed
from reconcile_receipt import reconcile_receipt
from publish_bundle import publish_bundle
from enrich_reservation import enrich_reservation
from summarize_header import summarize_header
from merge_summary import merge_summary
from load_roster import load_roster


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("pull_supplier_feed", pull_supplier_feed),
    path("reconcile_receipt", reconcile_receipt),
    path("publish_bundle", publish_bundle),
    path("enrich_reservation", enrich_reservation),
    path("summarize_header", summarize_header),
    path("merge_summary", merge_summary),
    path("load_roster", load_roster),
]
