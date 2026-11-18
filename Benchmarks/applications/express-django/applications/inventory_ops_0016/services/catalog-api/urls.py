from django.http import JsonResponse
from django.urls import path
from sku_lookup import lookup_sku
from collect_schedule import collect_schedule
from export_digest import export_digest
from rotate_threshold import rotate_threshold
from fetch_supplier import fetch_supplier
from summarize_reservation import summarize_reservation
from format_digest import format_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("lookup_sku", lookup_sku),
    path("collect_schedule", collect_schedule),
    path("export_digest", export_digest),
    path("rotate_threshold", rotate_threshold),
    path("fetch_supplier/<path_param>", fetch_supplier),
    path("summarize_reservation", summarize_reservation),
    path("format_digest", format_digest),
]
