from django.http import JsonResponse
from django.urls import path
from audit_append import append_audit
from load_header import load_header
from compact_flag import compact_flag
from export_flag import export_flag
from resolve_index import resolve_index
from annotate_secret import annotate_secret
from fetch_summary import fetch_summary
from build_index import build_index


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("append_audit", append_audit),
    path("load_header", load_header),
    path("compact_flag", compact_flag),
    path("export_flag", export_flag),
    path("resolve_index", resolve_index),
    path("annotate_secret", annotate_secret),
    path("fetch_summary", fetch_summary),
    path("build_index", build_index),
]
