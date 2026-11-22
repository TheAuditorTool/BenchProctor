from django.http import JsonResponse
from django.urls import path
from asset_upload import upload_asset
from summarize_record import summarize_record
from render_caption import render_caption
from export_profile import export_profile
from validate_schedule import validate_schedule
from validate_checkpoint import validate_checkpoint
from reconcile_report import reconcile_report


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("upload_asset", upload_asset),
    path("summarize_record", summarize_record),
    path("render_caption", render_caption),
    path("export_profile", export_profile),
    path("validate_schedule", validate_schedule),
    path("validate_checkpoint", validate_checkpoint),
    path("reconcile_report", reconcile_report),
]
