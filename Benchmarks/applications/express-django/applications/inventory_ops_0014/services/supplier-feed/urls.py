from django.http import JsonResponse
from django.urls import path
from supplier_feed import pull_supplier_feed
from load_record import load_record
from reconcile_index import reconcile_index
from rotate_profile import rotate_profile
from enrich_profile import enrich_profile
from validate_receipt import validate_receipt
from resolve_bundle import resolve_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("pull_supplier_feed", pull_supplier_feed),
    path("load_record", load_record),
    path("reconcile_index", reconcile_index),
    path("rotate_profile", rotate_profile),
    path("enrich_profile", enrich_profile),
    path("validate_receipt", validate_receipt),
    path("resolve_bundle", resolve_bundle),
]
