from django.http import JsonResponse
from django.urls import path
from tenant_provision import provision_tenant
from reconcile_checkpoint import reconcile_checkpoint
from compact_quota import compact_quota
from render_policy import render_policy
from validate_tenant import validate_tenant
from export_manifest import export_manifest
from annotate_report import annotate_report
from fetch_ledger import fetch_ledger


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("provision_tenant", provision_tenant),
    path("reconcile_checkpoint", reconcile_checkpoint),
    path("compact_quota", compact_quota),
    path("render_policy", render_policy),
    path("validate_tenant", validate_tenant),
    path("export_manifest", export_manifest),
    path("annotate_report/<path_param>", annotate_report),
    path("fetch_ledger", fetch_ledger),
]
