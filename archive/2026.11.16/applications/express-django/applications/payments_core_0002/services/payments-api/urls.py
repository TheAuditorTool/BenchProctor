from django.http import JsonResponse
from django.urls import path
from payment_authorize import authorize_payment
from format_window import format_window
from annotate_index import annotate_index
from load_batch import load_batch
from export_policy import export_policy
from rotate_payout import rotate_payout
from merge_profile import merge_profile


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("authorize_payment", authorize_payment),
    path("format_window", format_window),
    path("annotate_index", annotate_index),
    path("load_batch", load_batch),
    path("export_policy", export_policy),
    path("rotate_payout", rotate_payout),
    path("merge_profile", merge_profile),
]
