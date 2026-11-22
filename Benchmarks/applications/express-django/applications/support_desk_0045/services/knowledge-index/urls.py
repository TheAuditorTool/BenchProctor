from django.http import JsonResponse
from django.urls import path
from knowledge_search import search_knowledge
from summarize_receipt import summarize_receipt
from format_record import format_record
from summarize_checkpoint import summarize_checkpoint
from enrich_threshold import enrich_threshold
from load_ledger import load_ledger
from render_ticket import render_ticket
from fetch_window import fetch_window


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("search_knowledge", search_knowledge),
    path("summarize_receipt", summarize_receipt),
    path("format_record", format_record),
    path("summarize_checkpoint", summarize_checkpoint),
    path("enrich_threshold", enrich_threshold),
    path("load_ledger", load_ledger),
    path("render_ticket", render_ticket),
    path("fetch_window", fetch_window),
]
