from django.http import JsonResponse
from django.urls import path
from tenant_provision import provision_tenant
from compact_flag import compact_flag
from verify_digest import verify_digest
from enrich_digest import enrich_digest
from validate_bundle import validate_bundle
from archive_schedule import archive_schedule
from fetch_batch import fetch_batch
from annotate_profile import annotate_profile


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("provision_tenant", provision_tenant),
    path("compact_flag", compact_flag),
    path("verify_digest", verify_digest),
    path("enrich_digest", enrich_digest),
    path("validate_bundle", validate_bundle),
    path("archive_schedule", archive_schedule),
    path("fetch_batch", fetch_batch),
    path("annotate_profile", annotate_profile),
]
