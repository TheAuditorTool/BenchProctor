from django.http import JsonResponse
from django.urls import path
from survey_send import send_survey
from enrich_policy import enrich_policy
from audit_snapshot import audit_snapshot
from compact_record import compact_record
from merge_bundle import merge_bundle
from prune_manifest import prune_manifest
from fetch_header import fetch_header


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("send_survey", send_survey),
    path("enrich_policy", enrich_policy),
    path("audit_snapshot/<path_param>", audit_snapshot),
    path("compact_record", compact_record),
    path("merge_bundle", merge_bundle),
    path("prune_manifest", prune_manifest),
    path("fetch_header", fetch_header),
]
