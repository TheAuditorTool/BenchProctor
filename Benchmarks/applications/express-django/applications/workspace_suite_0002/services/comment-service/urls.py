from django.http import JsonResponse
from django.urls import path
from comment_post import post_comment
from load_snapshot import load_snapshot
from validate_config import validate_config
from load_digest import load_digest
from reconcile_snapshot import reconcile_snapshot
from export_policy import export_policy
from fetch_comment import fetch_comment


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("post_comment", post_comment),
    path("load_snapshot/<path_param>", load_snapshot),
    path("validate_config", validate_config),
    path("load_digest", load_digest),
    path("reconcile_snapshot", reconcile_snapshot),
    path("export_policy", export_policy),
    path("fetch_comment", fetch_comment),
]
