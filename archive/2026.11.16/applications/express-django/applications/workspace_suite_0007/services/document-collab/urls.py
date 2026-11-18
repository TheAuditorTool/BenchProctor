from django.http import JsonResponse
from django.urls import path
from document_edit import edit_document
from load_roster import load_roster
from load_record import load_record
from render_checkpoint import render_checkpoint
from enrich_digest import enrich_digest
from build_index import build_index
from load_summary import load_summary
from summarize_digest import summarize_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("edit_document", edit_document),
    path("load_roster", load_roster),
    path("load_record", load_record),
    path("render_checkpoint", render_checkpoint),
    path("enrich_digest", enrich_digest),
    path("build_index", build_index),
    path("load_summary", load_summary),
    path("summarize_digest", summarize_digest),
]
