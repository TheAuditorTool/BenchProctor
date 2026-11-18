from django.http import JsonResponse
from django.urls import path
from knowledge_search import search_knowledge
from load_report import load_report
from rotate_roster import rotate_roster
from summarize_checkpoint import summarize_checkpoint
from rotate_snapshot import rotate_snapshot
from collect_summary import collect_summary
from enrich_digest import enrich_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("search_knowledge", search_knowledge),
    path("load_report", load_report),
    path("rotate_roster", rotate_roster),
    path("summarize_checkpoint", summarize_checkpoint),
    path("rotate_snapshot", rotate_snapshot),
    path("collect_summary", collect_summary),
    path("enrich_digest", enrich_digest),
]
