from django.http import JsonResponse
from django.urls import path
from article_draft import draft_article
from audit_checkpoint import audit_checkpoint
from verify_digest import verify_digest
from fetch_header import fetch_header
from render_article import render_article
from resolve_batch import resolve_batch
from audit_header import audit_header
from rotate_ledger import rotate_ledger


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("draft_article", draft_article),
    path("audit_checkpoint", audit_checkpoint),
    path("verify_digest", verify_digest),
    path("fetch_header", fetch_header),
    path("render_article", render_article),
    path("resolve_batch", resolve_batch),
    path("audit_header", audit_header),
    path("rotate_ledger", rotate_ledger),
]
