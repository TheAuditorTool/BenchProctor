from django.http import JsonResponse
from django.urls import path
from knowledge_search import search_knowledge
from reconcile_batch import reconcile_batch
from normalize_report import normalize_report
from merge_index import merge_index
from merge_ledger import merge_ledger
from reconcile_receipt import reconcile_receipt
from export_config import export_config


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("search_knowledge", search_knowledge),
    path("reconcile_batch", reconcile_batch),
    path("normalize_report", normalize_report),
    path("merge_index", merge_index),
    path("merge_ledger", merge_ledger),
    path("reconcile_receipt", reconcile_receipt),
    path("export_config", export_config),
]
