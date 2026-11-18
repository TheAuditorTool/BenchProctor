from django.http import JsonResponse
from django.urls import path
from preview_render import render_preview
from annotate_summary import annotate_summary
from audit_checkpoint import audit_checkpoint
from prune_roster import prune_roster
from rotate_summary import rotate_summary
from render_config import render_config
from merge_snapshot import merge_snapshot
from merge_digest import merge_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("render_preview", render_preview),
    path("annotate_summary/<path_param>", annotate_summary),
    path("audit_checkpoint", audit_checkpoint),
    path("prune_roster", prune_roster),
    path("rotate_summary", rotate_summary),
    path("render_config", render_config),
    path("merge_snapshot", merge_snapshot),
    path("merge_digest", merge_digest),
]
