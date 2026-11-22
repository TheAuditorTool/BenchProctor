from django.http import JsonResponse
from django.urls import path
from ticket_route import route_ticket
from collect_receipt import collect_receipt
from rotate_checkpoint import rotate_checkpoint
from verify_roster import verify_roster
from render_checkpoint import render_checkpoint
from prune_policy import prune_policy
from fetch_manifest import fetch_manifest
from enrich_ticket import enrich_ticket


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("route_ticket", route_ticket),
    path("collect_receipt", collect_receipt),
    path("rotate_checkpoint", rotate_checkpoint),
    path("verify_roster", verify_roster),
    path("render_checkpoint", render_checkpoint),
    path("prune_policy", prune_policy),
    path("fetch_manifest", fetch_manifest),
    path("enrich_ticket", enrich_ticket),
]
