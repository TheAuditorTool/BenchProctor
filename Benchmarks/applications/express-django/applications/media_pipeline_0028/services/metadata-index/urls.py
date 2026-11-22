from django.http import JsonResponse
from django.urls import path
from metadata_index import index_metadata
from fetch_profile import fetch_profile
from rotate_receipt import rotate_receipt
from verify_record import verify_record
from enrich_roster import enrich_roster
from load_threshold import load_threshold
from resolve_receipt import resolve_receipt


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("index_metadata", index_metadata),
    path("fetch_profile", fetch_profile),
    path("rotate_receipt", rotate_receipt),
    path("verify_record", verify_record),
    path("enrich_roster", enrich_roster),
    path("load_threshold", load_threshold),
    path("resolve_receipt", resolve_receipt),
]
