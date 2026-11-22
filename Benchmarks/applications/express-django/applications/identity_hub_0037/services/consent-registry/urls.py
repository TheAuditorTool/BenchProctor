from django.http import JsonResponse
from django.urls import path
from consent_record import record_consent
from merge_policy import merge_policy
from prune_policy import prune_policy
from audit_digest import audit_digest
from validate_manifest import validate_manifest
from summarize_schedule import summarize_schedule
from enrich_config import enrich_config
from collect_snapshot import collect_snapshot


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("record_consent", record_consent),
    path("merge_policy", merge_policy),
    path("prune_policy", prune_policy),
    path("audit_digest", audit_digest),
    path("validate_manifest", validate_manifest),
    path("summarize_schedule", summarize_schedule),
    path("enrich_config", enrich_config),
    path("collect_snapshot", collect_snapshot),
]
