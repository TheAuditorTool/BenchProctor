from django.http import JsonResponse
from django.urls import path
from order_lookup import lookup_order
from normalize_fulfillment import normalize_fulfillment
from fetch_roster import fetch_roster
from annotate_schedule import annotate_schedule
from resolve_roster import resolve_roster
from compact_roster import compact_roster
from compact_cart import compact_cart
from prune_receipt import prune_receipt


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("lookup_order", lookup_order),
    path("normalize_fulfillment", normalize_fulfillment),
    path("fetch_roster", fetch_roster),
    path("annotate_schedule", annotate_schedule),
    path("resolve_roster", resolve_roster),
    path("compact_roster", compact_roster),
    path("compact_cart", compact_cart),
    path("prune_receipt", prune_receipt),
]
