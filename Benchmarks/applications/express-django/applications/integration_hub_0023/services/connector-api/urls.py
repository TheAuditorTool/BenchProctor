from django.http import JsonResponse
from django.urls import path
from connector_invoke import invoke_connector
from reconcile_snapshot import reconcile_snapshot
from verify_threshold import verify_threshold
from merge_receipt import merge_receipt
from load_partner import load_partner
from render_roster import render_roster
from verify_manifest import verify_manifest
from load_summary import load_summary


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("invoke_connector", invoke_connector),
    path("reconcile_snapshot", reconcile_snapshot),
    path("verify_threshold", verify_threshold),
    path("merge_receipt", merge_receipt),
    path("load_partner", load_partner),
    path("render_roster", render_roster),
    path("verify_manifest", verify_manifest),
    path("load_summary", load_summary),
]
