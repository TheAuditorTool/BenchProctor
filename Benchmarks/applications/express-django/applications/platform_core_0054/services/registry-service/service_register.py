# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
import json
from app_runtime import db


@csrf_exempt
def register_service(request):
    caption = json.loads(request.body or b'{}').get("platform_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", caption):
        return JsonResponse({'error': 'forbidden'}, status=400)
    handshake = caption
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
