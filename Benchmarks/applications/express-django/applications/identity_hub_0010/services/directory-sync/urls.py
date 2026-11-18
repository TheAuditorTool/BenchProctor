from django.http import JsonResponse
from django.urls import path
from directory_sync import sync_directory
from verify_checkpoint import verify_checkpoint
from normalize_session import normalize_session
from audit_schedule import audit_schedule
from validate_record import validate_record
from reconcile_batch import reconcile_batch
from verify_schedule import verify_schedule


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("sync_directory", sync_directory),
    path("verify_checkpoint", verify_checkpoint),
    path("normalize_session", normalize_session),
    path("audit_schedule", audit_schedule),
    path("validate_record", validate_record),
    path("reconcile_batch", reconcile_batch),
    path("verify_schedule", verify_schedule),
]
