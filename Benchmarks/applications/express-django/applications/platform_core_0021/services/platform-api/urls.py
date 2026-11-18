from django.http import JsonResponse
from django.urls import path
from tenant_provision import provision_tenant
from audit_threshold import audit_threshold
from export_record import export_record
from normalize_profile import normalize_profile
from export_window import export_window
from verify_checkpoint import verify_checkpoint
from resolve_report import resolve_report
from merge_window import merge_window


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("provision_tenant", provision_tenant),
    path("audit_threshold", audit_threshold),
    path("export_record/<path_param>", export_record),
    path("normalize_profile/<path_param>", normalize_profile),
    path("export_window", export_window),
    path("verify_checkpoint", verify_checkpoint),
    path("resolve_report", resolve_report),
    path("merge_window", merge_window),
]
