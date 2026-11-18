from django.http import JsonResponse
from django.urls import path
from escalation_raise import raise_escalation
from load_threshold import load_threshold
from audit_header import audit_header
from audit_escalation import audit_escalation
from validate_checkpoint import validate_checkpoint
from merge_ticket import merge_ticket
from build_header import build_header


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("raise_escalation", raise_escalation),
    path("load_threshold", load_threshold),
    path("audit_header", audit_header),
    path("audit_escalation", audit_escalation),
    path("validate_checkpoint", validate_checkpoint),
    path("merge_ticket", merge_ticket),
    path("build_header", build_header),
]
