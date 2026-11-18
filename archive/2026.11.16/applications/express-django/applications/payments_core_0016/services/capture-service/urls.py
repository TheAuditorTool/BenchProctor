from django.http import JsonResponse
from django.urls import path
from capture_settle import settle_capture
from compact_index import compact_index
from compact_record import compact_record
from verify_ledger import verify_ledger
from load_policy import load_policy
from render_window import render_window
from format_config import format_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("settle_capture", settle_capture),
    path("compact_index", compact_index),
    path("compact_record", compact_record),
    path("verify_ledger", verify_ledger),
    path("load_policy", load_policy),
    path("render_window", render_window),
    path("format_config", format_config),
]
