from django.http import JsonResponse
from django.urls import path
from bounce_record import record_bounce
from build_receipt import build_receipt
from reconcile_index import reconcile_index
from fetch_record import fetch_record
from resolve_index import resolve_index
from verify_profile import verify_profile
from verify_summary import verify_summary
from export_receipt import export_receipt


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("record_bounce", record_bounce),
    path("build_receipt", build_receipt),
    path("reconcile_index", reconcile_index),
    path("fetch_record", fetch_record),
    path("resolve_index", resolve_index),
    path("verify_profile", verify_profile),
    path("verify_summary", verify_summary),
    path("export_receipt", export_receipt),
]
