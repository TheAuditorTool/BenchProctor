# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def render_window(request):
    synopsis = request.FILES['upload'].name
    handshake = (lambda v: v.strip())(synopsis)
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
