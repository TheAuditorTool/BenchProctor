from django.http import JsonResponse
from django.urls import path
from fx_convert import convert_fx
from compact_receipt import compact_receipt
from merge_snapshot import merge_snapshot
from normalize_dispute import normalize_dispute
from reconcile_config import reconcile_config
from format_policy import format_policy
from validate_receipt import validate_receipt


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("convert_fx", convert_fx),
    path("compact_receipt", compact_receipt),
    path("merge_snapshot", merge_snapshot),
    path("normalize_dispute", normalize_dispute),
    path("reconcile_config", reconcile_config),
    path("format_policy/<path_param>", format_policy),
    path("validate_receipt", validate_receipt),
]
