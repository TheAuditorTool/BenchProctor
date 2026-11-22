from django.http import JsonResponse
from django.urls import path
from share_grant import grant_share
from normalize_policy import normalize_policy
from prune_workspace import prune_workspace
from reconcile_digest import reconcile_digest
from compact_report import compact_report
from merge_ledger import merge_ledger
from validate_comment import validate_comment
from normalize_record import normalize_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("grant_share", grant_share),
    path("normalize_policy", normalize_policy),
    path("prune_workspace", prune_workspace),
    path("reconcile_digest", reconcile_digest),
    path("compact_report", compact_report),
    path("merge_ledger", merge_ledger),
    path("validate_comment", validate_comment),
    path("normalize_record", normalize_record),
]
