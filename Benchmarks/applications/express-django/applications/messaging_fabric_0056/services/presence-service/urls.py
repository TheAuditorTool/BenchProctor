from django.http import JsonResponse
from django.urls import path
from presence_update import update_presence
from format_header import format_header
from collect_bundle import collect_bundle
from merge_ledger import merge_ledger
from load_message import load_message
from verify_header import verify_header
from load_record import load_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("update_presence", update_presence),
    path("format_header/<path_param>", format_header),
    path("collect_bundle", collect_bundle),
    path("merge_ledger", merge_ledger),
    path("load_message", load_message),
    path("verify_header", verify_header),
    path("load_record", load_record),
]
