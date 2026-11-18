from django.http import JsonResponse
from django.urls import path
from payment_authorize import authorize_payment
from publish_payout import publish_payout
from audit_snapshot import audit_snapshot
from merge_batch import merge_batch
from merge_receipt import merge_receipt
from rotate_threshold import rotate_threshold
from load_record import load_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("authorize_payment", authorize_payment),
    path("publish_payout", publish_payout),
    path("audit_snapshot", audit_snapshot),
    path("merge_batch", merge_batch),
    path("merge_receipt", merge_receipt),
    path("rotate_threshold", rotate_threshold),
    path("load_record", load_record),
]
