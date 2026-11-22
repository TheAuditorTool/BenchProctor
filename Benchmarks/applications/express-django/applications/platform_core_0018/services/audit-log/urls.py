from django.http import JsonResponse
from django.urls import path
from audit_append import append_audit
from render_secret import render_secret
from validate_tenant import validate_tenant
from normalize_flag import normalize_flag
from archive_checkpoint import archive_checkpoint
from validate_policy import validate_policy
from fetch_roster import fetch_roster


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("append_audit", append_audit),
    path("render_secret", render_secret),
    path("validate_tenant", validate_tenant),
    path("normalize_flag", normalize_flag),
    path("archive_checkpoint", archive_checkpoint),
    path("validate_policy", validate_policy),
    path("fetch_roster", fetch_roster),
]
