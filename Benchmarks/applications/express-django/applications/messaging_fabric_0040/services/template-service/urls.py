from django.http import JsonResponse
from django.urls import path
from template_compose import compose_template
from annotate_window import annotate_window
from normalize_profile import normalize_profile
from collect_summary import collect_summary
from prune_roster import prune_roster
from validate_schedule import validate_schedule
from verify_delivery import verify_delivery


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("compose_template", compose_template),
    path("annotate_window/<path_param>", annotate_window),
    path("normalize_profile", normalize_profile),
    path("collect_summary", collect_summary),
    path("prune_roster", prune_roster),
    path("validate_schedule", validate_schedule),
    path("verify_delivery/<path_param>", verify_delivery),
]
