from django.http import JsonResponse
from django.urls import path
from share_grant import grant_share
from annotate_digest import annotate_digest
from rotate_digest import rotate_digest
from export_digest import export_digest
from format_comment import format_comment
from prune_schedule import prune_schedule
from fetch_digest import fetch_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("grant_share", grant_share),
    path("annotate_digest", annotate_digest),
    path("rotate_digest", rotate_digest),
    path("export_digest", export_digest),
    path("format_comment", format_comment),
    path("prune_schedule", prune_schedule),
    path("fetch_digest", fetch_digest),
]
