from django.http import JsonResponse
from django.urls import path
from carrier_dispatch import dispatch_carrier
from fetch_profile import fetch_profile
from audit_shipment import audit_shipment
from verify_carrier import verify_carrier
from rotate_label import rotate_label
from enrich_roster import enrich_roster
from collect_label import collect_label
from validate_policy import validate_policy


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("dispatch_carrier", dispatch_carrier),
    path("fetch_profile", fetch_profile),
    path("audit_shipment/<path_param>", audit_shipment),
    path("verify_carrier", verify_carrier),
    path("rotate_label", rotate_label),
    path("enrich_roster", enrich_roster),
    path("collect_label", collect_label),
    path("validate_policy", validate_policy),
]
