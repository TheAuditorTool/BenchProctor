from django.http import JsonResponse
from django.urls import path
from ledger_post import post_ledger_entry
from validate_header import validate_header
from archive_index import archive_index
from validate_summary import validate_summary
from load_roster import load_roster
from export_dunning import export_dunning
from export_batch import export_batch
from validate_window import validate_window


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("post_ledger_entry", post_ledger_entry),
    path("validate_header", validate_header),
    path("archive_index", archive_index),
    path("validate_summary", validate_summary),
    path("load_roster", load_roster),
    path("export_dunning", export_dunning),
    path("export_batch", export_batch),
    path("validate_window", validate_window),
]
