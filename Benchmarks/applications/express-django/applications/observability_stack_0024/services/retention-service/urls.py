from django.http import JsonResponse
from django.urls import path
from retention_sweep import sweep_retention
from load_window import load_window
from reconcile_report import reconcile_report
from enrich_window import enrich_window
from rotate_digest import rotate_digest
from export_summary import export_summary
from audit_bundle import audit_bundle


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("sweep_retention", sweep_retention),
    path("load_window", load_window),
    path("reconcile_report", reconcile_report),
    path("enrich_window", enrich_window),
    path("rotate_digest", rotate_digest),
    path("export_summary", export_summary),
    path("audit_bundle", audit_bundle),
]
