from django.http import JsonResponse
from django.urls import path
from dunning_notice import send_dunning_notice
from enrich_summary import enrich_summary
from build_invoice import build_invoice
from merge_statement import merge_statement
from render_receipt import render_receipt
from rotate_record import rotate_record
from collect_ledger import collect_ledger
from validate_dunning import validate_dunning


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("send_dunning_notice", send_dunning_notice),
    path("enrich_summary", enrich_summary),
    path("build_invoice", build_invoice),
    path("merge_statement", merge_statement),
    path("render_receipt", render_receipt),
    path("rotate_record", rotate_record),
    path("collect_ledger", collect_ledger),
    path("validate_dunning", validate_dunning),
]
