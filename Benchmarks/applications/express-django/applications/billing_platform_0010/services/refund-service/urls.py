from django.http import JsonResponse
from django.urls import path
from refund_issue import issue_refund
from audit_bundle import audit_bundle
from export_summary import export_summary
from export_header import export_header
from format_statement import format_statement
from compact_dunning import compact_dunning
from compact_digest import compact_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("issue_refund", issue_refund),
    path("audit_bundle", audit_bundle),
    path("export_summary", export_summary),
    path("export_header", export_header),
    path("format_statement", format_statement),
    path("compact_dunning", compact_dunning),
    path("compact_digest", compact_digest),
]
