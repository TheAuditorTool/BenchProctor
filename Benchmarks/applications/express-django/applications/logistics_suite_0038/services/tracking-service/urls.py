from django.http import JsonResponse
from django.urls import path
from tracking_poll import poll_tracking
from validate_profile import validate_profile
from prune_label import prune_label
from enrich_header import enrich_header
from compact_shipment import compact_shipment
from enrich_summary import enrich_summary
from reconcile_config import reconcile_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("poll_tracking", poll_tracking),
    path("validate_profile/<path_param>", validate_profile),
    path("prune_label", prune_label),
    path("enrich_header", enrich_header),
    path("compact_shipment", compact_shipment),
    path("enrich_summary", enrich_summary),
    path("reconcile_config", reconcile_config),
]
