from django.http import JsonResponse
from django.urls import path
from decision_record import record_decision
from render_rule import render_rule
from publish_report import publish_report
from audit_threshold import audit_threshold
from merge_roster import merge_roster
from verify_profile import verify_profile
from merge_digest import merge_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("record_decision", record_decision),
    path("render_rule", render_rule),
    path("publish_report", publish_report),
    path("audit_threshold", audit_threshold),
    path("merge_roster", merge_roster),
    path("verify_profile", verify_profile),
    path("merge_digest", merge_digest),
]
