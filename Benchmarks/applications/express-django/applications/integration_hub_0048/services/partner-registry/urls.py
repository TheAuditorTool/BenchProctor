from django.http import JsonResponse
from django.urls import path
from partner_register import register_partner
from enrich_config import enrich_config
from publish_roster import publish_roster
from verify_connector import verify_connector
from archive_header import archive_header
from audit_window import audit_window
from normalize_index import normalize_index


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("register_partner", register_partner),
    path("enrich_config/<path_param>", enrich_config),
    path("publish_roster", publish_roster),
    path("verify_connector", verify_connector),
    path("archive_header", archive_header),
    path("audit_window", audit_window),
    path("normalize_index", normalize_index),
]
