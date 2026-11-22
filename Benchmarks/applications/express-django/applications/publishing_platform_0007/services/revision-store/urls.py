from django.http import JsonResponse
from django.urls import path
from revision_save import save_revision
from build_index import build_index
from archive_record import archive_record
from build_ledger import build_ledger
from publish_article import publish_article
from validate_taxonomy import validate_taxonomy
from build_window import build_window


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("save_revision", save_revision),
    path("build_index", build_index),
    path("archive_record", archive_record),
    path("build_ledger", build_ledger),
    path("publish_article", publish_article),
    path("validate_taxonomy", validate_taxonomy),
    path("build_window", build_window),
]
