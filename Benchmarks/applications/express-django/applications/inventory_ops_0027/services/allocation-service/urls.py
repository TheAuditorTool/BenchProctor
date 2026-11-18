from django.http import JsonResponse
from django.urls import path
from allocation_solve import solve_allocation
from audit_supplier import audit_supplier
from summarize_allocation import summarize_allocation
from validate_schedule import validate_schedule
from reconcile_config import reconcile_config
from reconcile_digest import reconcile_digest
from merge_threshold import merge_threshold
from prune_allocation import prune_allocation


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("solve_allocation", solve_allocation),
    path("audit_supplier", audit_supplier),
    path("summarize_allocation", summarize_allocation),
    path("validate_schedule", validate_schedule),
    path("reconcile_config", reconcile_config),
    path("reconcile_digest", reconcile_digest),
    path("merge_threshold", merge_threshold),
    path("prune_allocation", prune_allocation),
]
