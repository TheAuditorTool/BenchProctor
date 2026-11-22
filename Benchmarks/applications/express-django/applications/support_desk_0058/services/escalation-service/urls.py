from django.http import JsonResponse
from django.urls import path
from escalation_raise import raise_escalation
from publish_threshold import publish_threshold
from load_threshold import load_threshold
from load_escalation import load_escalation
from resolve_summary import resolve_summary
from audit_schedule import audit_schedule
from audit_config import audit_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("raise_escalation", raise_escalation),
    path("publish_threshold", publish_threshold),
    path("load_threshold", load_threshold),
    path("load_escalation", load_escalation),
    path("resolve_summary", resolve_summary),
    path("audit_schedule", audit_schedule),
    path("audit_config", audit_config),
]
