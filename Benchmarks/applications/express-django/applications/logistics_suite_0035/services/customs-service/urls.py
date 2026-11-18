from django.http import JsonResponse
from django.urls import path
from customs_declare import declare_customs
from export_index import export_index
from rotate_checkpoint import rotate_checkpoint
from enrich_bundle import enrich_bundle
from export_roster import export_roster
from format_policy import format_policy
from enrich_roster import enrich_roster
from export_summary import export_summary


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("declare_customs", declare_customs),
    path("export_index", export_index),
    path("rotate_checkpoint", rotate_checkpoint),
    path("enrich_bundle/<path_param>", enrich_bundle),
    path("export_roster", export_roster),
    path("format_policy", format_policy),
    path("enrich_roster", enrich_roster),
    path("export_summary", export_summary),
]
