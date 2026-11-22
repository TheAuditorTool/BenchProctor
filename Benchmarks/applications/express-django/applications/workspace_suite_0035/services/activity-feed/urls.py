from django.http import JsonResponse
from django.urls import path
from activity_stream import stream_activity
from load_index import load_index
from rotate_profile import rotate_profile
from audit_membership import audit_membership
from annotate_policy import annotate_policy
from normalize_record import normalize_record
from collect_threshold import collect_threshold
from annotate_snapshot import annotate_snapshot


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("stream_activity", stream_activity),
    path("load_index", load_index),
    path("rotate_profile", rotate_profile),
    path("audit_membership", audit_membership),
    path("annotate_policy", annotate_policy),
    path("normalize_record", normalize_record),
    path("collect_threshold", collect_threshold),
    path("annotate_snapshot", annotate_snapshot),
]
