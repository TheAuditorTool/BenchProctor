from django.http import JsonResponse
from django.urls import path
from return_request import request_return
from compact_window import compact_window
from archive_ledger import archive_ledger
from export_window import export_window
from collect_ledger import collect_ledger
from rotate_window import rotate_window
from compact_record import compact_record


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("request_return", request_return),
    path("compact_window", compact_window),
    path("archive_ledger", archive_ledger),
    path("export_window", export_window),
    path("collect_ledger", collect_ledger),
    path("rotate_window", rotate_window),
    path("compact_record", compact_record),
]
