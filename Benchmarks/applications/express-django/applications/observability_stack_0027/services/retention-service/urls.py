from django.http import JsonResponse
from django.urls import path
from retention_sweep import sweep_retention
from summarize_manifest import summarize_manifest
from enrich_receipt import enrich_receipt
from merge_receipt import merge_receipt
from render_manifest import render_manifest
from compact_batch import compact_batch
from load_batch import load_batch
from normalize_trace import normalize_trace


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("sweep_retention", sweep_retention),
    path("summarize_manifest", summarize_manifest),
    path("enrich_receipt", enrich_receipt),
    path("merge_receipt", merge_receipt),
    path("render_manifest", render_manifest),
    path("compact_batch", compact_batch),
    path("load_batch", load_batch),
    path("normalize_trace", normalize_trace),
]
