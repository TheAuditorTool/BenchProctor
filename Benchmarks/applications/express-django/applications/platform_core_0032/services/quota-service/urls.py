from django.http import JsonResponse
from django.urls import path
from quota_enforce import enforce_quota
from archive_summary import archive_summary
from collect_header import collect_header
from publish_threshold import publish_threshold
from export_schedule import export_schedule
from summarize_window import summarize_window
from audit_secret import audit_secret


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("enforce_quota", enforce_quota),
    path("archive_summary", archive_summary),
    path("collect_header", collect_header),
    path("publish_threshold", publish_threshold),
    path("export_schedule", export_schedule),
    path("summarize_window", summarize_window),
    path("audit_secret", audit_secret),
]
