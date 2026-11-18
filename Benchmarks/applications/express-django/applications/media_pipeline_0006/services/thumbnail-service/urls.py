from django.http import JsonResponse
from django.urls import path
from thumbnail_render import render_thumbnail
from fetch_ledger import fetch_ledger
from build_roster import build_roster
from render_schedule import render_schedule
from annotate_caption import annotate_caption
from load_threshold import load_threshold
from rotate_index import rotate_index


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("render_thumbnail", render_thumbnail),
    path("fetch_ledger", fetch_ledger),
    path("build_roster", build_roster),
    path("render_schedule", render_schedule),
    path("annotate_caption", annotate_caption),
    path("load_threshold", load_threshold),
    path("rotate_index", rotate_index),
]
