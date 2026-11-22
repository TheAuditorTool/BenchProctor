from django.http import JsonResponse
from django.urls import path
from delivery_dispatch import dispatch_delivery
from load_subscription import load_subscription
from publish_roster import publish_roster
from archive_receipt import archive_receipt
from enrich_delivery import enrich_delivery
from resolve_window import resolve_window
from compact_profile import compact_profile


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("dispatch_delivery", dispatch_delivery),
    path("load_subscription", load_subscription),
    path("publish_roster", publish_roster),
    path("archive_receipt", archive_receipt),
    path("enrich_delivery", enrich_delivery),
    path("resolve_window", resolve_window),
    path("compact_profile", compact_profile),
]
