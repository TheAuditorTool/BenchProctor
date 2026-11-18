from django.http import JsonResponse
from django.urls import path
from payment_capture import capture_payment
from render_batch import render_batch
from build_summary import build_summary
from render_snapshot import render_snapshot
from annotate_policy import annotate_policy
from render_invoice import render_invoice
from build_ledger import build_ledger


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("capture_payment", capture_payment),
    path("render_batch", render_batch),
    path("build_summary", build_summary),
    path("render_snapshot", render_snapshot),
    path("annotate_policy", annotate_policy),
    path("render_invoice", render_invoice),
    path("build_ledger", build_ledger),
]
