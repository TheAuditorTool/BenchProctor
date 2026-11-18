from django.http import JsonResponse
from django.urls import path
from knowledge_search import search_knowledge
from collect_summary import collect_summary
from render_macro import render_macro
from enrich_digest import enrich_digest
from rotate_bundle import rotate_bundle
from publish_receipt import publish_receipt
from compact_batch import compact_batch
from enrich_ticket import enrich_ticket


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("search_knowledge", search_knowledge),
    path("collect_summary", collect_summary),
    path("render_macro", render_macro),
    path("enrich_digest", enrich_digest),
    path("rotate_bundle", rotate_bundle),
    path("publish_receipt", publish_receipt),
    path("compact_batch", compact_batch),
    path("enrich_ticket", enrich_ticket),
]
