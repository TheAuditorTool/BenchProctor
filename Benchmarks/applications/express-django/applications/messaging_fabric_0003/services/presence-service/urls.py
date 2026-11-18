from django.http import JsonResponse
from django.urls import path
from presence_update import update_presence
from annotate_report import annotate_report
from export_bundle import export_bundle
from fetch_bundle import fetch_bundle
from audit_batch import audit_batch
from enrich_record import enrich_record
from normalize_record import normalize_record
from enrich_delivery import enrich_delivery


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("update_presence", update_presence),
    path("annotate_report", annotate_report),
    path("export_bundle", export_bundle),
    path("fetch_bundle", fetch_bundle),
    path("audit_batch", audit_batch),
    path("enrich_record", enrich_record),
    path("normalize_record", normalize_record),
    path("enrich_delivery", enrich_delivery),
]
