from django.http import JsonResponse
from django.urls import path
from reconcile_batch import run_reconciliation
from export_payout import export_payout
from normalize_index import normalize_index
from enrich_header import enrich_header
from enrich_config import enrich_config
from reconcile_digest import reconcile_digest
from resolve_config import resolve_config
from annotate_index import annotate_index


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("run_reconciliation", run_reconciliation),
    path("export_payout", export_payout),
    path("normalize_index", normalize_index),
    path("enrich_header", enrich_header),
    path("enrich_config", enrich_config),
    path("reconcile_digest", reconcile_digest),
    path("resolve_config", resolve_config),
    path("annotate_index", annotate_index),
]
