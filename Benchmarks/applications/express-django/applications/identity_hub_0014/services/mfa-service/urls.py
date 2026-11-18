from django.http import JsonResponse
from django.urls import path
from mfa_verify import verify_mfa
from verify_config import verify_config
from resolve_bundle import resolve_bundle
from load_record import load_record
from collect_receipt import collect_receipt
from archive_checkpoint import archive_checkpoint
from load_digest import load_digest


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("verify_mfa", verify_mfa),
    path("verify_config", verify_config),
    path("resolve_bundle", resolve_bundle),
    path("load_record", load_record),
    path("collect_receipt", collect_receipt),
    path("archive_checkpoint", archive_checkpoint),
    path("load_digest", load_digest),
]
