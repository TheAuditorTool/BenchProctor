from django.http import JsonResponse
from django.urls import path
from field_mapping import map_field
from collect_bundle import collect_bundle
from format_partner import format_partner
from audit_report import audit_report
from enrich_snapshot import enrich_snapshot
from export_snapshot import export_snapshot
from rotate_digest import rotate_digest
from publish_batch import publish_batch


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("map_field", map_field),
    path("collect_bundle", collect_bundle),
    path("format_partner", format_partner),
    path("audit_report", audit_report),
    path("enrich_snapshot", enrich_snapshot),
    path("export_snapshot", export_snapshot),
    path("rotate_digest", rotate_digest),
    path("publish_batch", publish_batch),
]
