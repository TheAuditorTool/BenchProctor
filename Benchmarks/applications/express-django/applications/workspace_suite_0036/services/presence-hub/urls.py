from django.http import JsonResponse
from django.urls import path
from presence_track import track_presence
from resolve_receipt import resolve_receipt
from rotate_document import rotate_document
from build_window import build_window
from annotate_report import annotate_report
from compact_window import compact_window
from verify_receipt import verify_receipt


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health", health),
    path("track_presence", track_presence),
    path("resolve_receipt", resolve_receipt),
    path("rotate_document", rotate_document),
    path("build_window", build_window),
    path("annotate_report", annotate_report),
    path("compact_window", compact_window),
    path("verify_receipt", verify_receipt),
]
