from django.http import JsonResponse
from django.urls import path
from payment_capture import capture_payment
from compact_policy import compact_policy
from publish_invoice import publish_invoice
from validate_receipt import validate_receipt
from fetch_invoice import fetch_invoice
from rotate_snapshot import rotate_snapshot
from normalize_policy import normalize_policy
from summarize_profile import summarize_profile


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("capture_payment", capture_payment),
    path("compact_policy", compact_policy),
    path("publish_invoice/<path_param>", publish_invoice),
    path("validate_receipt", validate_receipt),
    path("fetch_invoice", fetch_invoice),
    path("rotate_snapshot", rotate_snapshot),
    path("normalize_policy", normalize_policy),
    path("summarize_profile", summarize_profile),
]
