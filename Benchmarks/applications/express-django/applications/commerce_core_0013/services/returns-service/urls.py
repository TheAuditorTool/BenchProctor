from django.http import JsonResponse
from django.urls import path
from return_request import request_return
from compact_record import compact_record
from annotate_order import annotate_order
from normalize_receipt import normalize_receipt
from reconcile_policy import reconcile_policy
from rotate_index import rotate_index
from audit_roster import audit_roster
from render_bundle import render_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("request_return", request_return),
    path("compact_record", compact_record),
    path("annotate_order", annotate_order),
    path("normalize_receipt", normalize_receipt),
    path("reconcile_policy", reconcile_policy),
    path("rotate_index", rotate_index),
    path("audit_roster", audit_roster),
    path("render_bundle", render_bundle),
]
