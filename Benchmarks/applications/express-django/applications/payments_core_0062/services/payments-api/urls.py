from django.http import JsonResponse
from django.urls import path
from payment_authorize import authorize_payment
from publish_dispute import publish_dispute
from archive_digest import archive_digest
from annotate_header import annotate_header
from publish_summary import publish_summary
from build_digest import build_digest
from format_window import format_window


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("authorize_payment", authorize_payment),
    path("publish_dispute", publish_dispute),
    path("archive_digest", archive_digest),
    path("annotate_header", annotate_header),
    path("publish_summary", publish_summary),
    path("build_digest", build_digest),
    path("format_window", format_window),
]
