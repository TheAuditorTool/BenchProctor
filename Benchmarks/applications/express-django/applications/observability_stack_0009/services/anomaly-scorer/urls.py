from django.http import JsonResponse
from django.urls import path
from anomaly_score import score_anomaly
from build_policy import build_policy
from reconcile_roster import reconcile_roster
from compact_digest import compact_digest
from fetch_trace import fetch_trace
from reconcile_bundle import reconcile_bundle
from format_digest import format_digest
from audit_config import audit_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("score_anomaly", score_anomaly),
    path("build_policy", build_policy),
    path("reconcile_roster", reconcile_roster),
    path("compact_digest", compact_digest),
    path("fetch_trace", fetch_trace),
    path("reconcile_bundle", reconcile_bundle),
    path("format_digest", format_digest),
    path("audit_config", audit_config),
]
