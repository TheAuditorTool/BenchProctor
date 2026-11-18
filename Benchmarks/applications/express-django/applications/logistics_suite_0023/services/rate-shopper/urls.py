from django.http import JsonResponse
from django.urls import path
from rate_shop import shop_rate
from archive_config import archive_config
from collect_label import collect_label
from load_header import load_header
from prune_shipment import prune_shipment
from build_snapshot import build_snapshot
from archive_snapshot import archive_snapshot
from enrich_carrier import enrich_carrier


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("shop_rate", shop_rate),
    path("archive_config", archive_config),
    path("collect_label/<path_param>", collect_label),
    path("load_header", load_header),
    path("prune_shipment", prune_shipment),
    path("build_snapshot", build_snapshot),
    path("archive_snapshot", archive_snapshot),
    path("enrich_carrier", enrich_carrier),
]
