# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
from app_runtime import db


@csrf_exempt
def collect_bundle(request):
    heading = request.GET.get('id', '')
    handshake = unquote(heading)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': handshake})
    return JsonResponse({"saved": True})
