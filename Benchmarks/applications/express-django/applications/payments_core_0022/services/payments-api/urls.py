from django.http import JsonResponse
from django.urls import path
from payment_authorize import authorize_payment
from annotate_snapshot import annotate_snapshot
from enrich_schedule import enrich_schedule
from archive_policy import archive_policy
from audit_threshold import audit_threshold
from summarize_threshold import summarize_threshold
from fetch_record import fetch_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("authorize_payment", authorize_payment),
    path("annotate_snapshot", annotate_snapshot),
    path("enrich_schedule/<path_param>", enrich_schedule),
    path("archive_policy", archive_policy),
    path("audit_threshold", audit_threshold),
    path("summarize_threshold", summarize_threshold),
    path("fetch_record", fetch_record),
]
