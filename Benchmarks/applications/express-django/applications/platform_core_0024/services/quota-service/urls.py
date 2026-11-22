from django.http import JsonResponse
from django.urls import path
from quota_enforce import enforce_quota
from build_policy import build_policy
from reconcile_policy import reconcile_policy
from collect_threshold import collect_threshold
from format_schedule import format_schedule
from load_policy import load_policy
from validate_quota import validate_quota


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("enforce_quota", enforce_quota),
    path("build_policy", build_policy),
    path("reconcile_policy", reconcile_policy),
    path("collect_threshold", collect_threshold),
    path("format_schedule", format_schedule),
    path("load_policy", load_policy),
    path("validate_quota", validate_quota),
]
