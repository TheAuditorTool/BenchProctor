from django.http import JsonResponse
from django.urls import path
from sku_lookup import lookup_sku
from archive_profile import archive_profile
from enrich_index import enrich_index
from compact_index import compact_index
from validate_batch import validate_batch
from validate_roster import validate_roster
from reconcile_record import reconcile_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("lookup_sku", lookup_sku),
    path("archive_profile", archive_profile),
    path("enrich_index", enrich_index),
    path("compact_index", compact_index),
    path("validate_batch/<path_param>", validate_batch),
    path("validate_roster", validate_roster),
    path("reconcile_record", reconcile_record),
]
