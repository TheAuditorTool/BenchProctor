from django.http import JsonResponse
from django.urls import path
from address_validate import validate_address
from summarize_label import summarize_label
from validate_report import validate_report
from format_batch import format_batch
from audit_checkpoint import audit_checkpoint
from annotate_window import annotate_window
from publish_record import publish_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("validate_address", validate_address),
    path("summarize_label/<path_param>", summarize_label),
    path("validate_report", validate_report),
    path("format_batch", format_batch),
    path("audit_checkpoint", audit_checkpoint),
    path("annotate_window", annotate_window),
    path("publish_record", publish_record),
]
