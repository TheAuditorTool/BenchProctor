# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
from app_runtime import db


@csrf_exempt
def format_mapping(request):
    wording = request.COOKIES.get('session_token', '')
    handshake = base64.b64decode(wording).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
