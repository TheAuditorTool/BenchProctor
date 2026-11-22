# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
from app_runtime import db


@csrf_exempt
def merge_rule(request):
    excerpt = request.COOKIES.get('session_token', '')
    verdict = base64.b64decode(excerpt).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(verdict) + "'")
    return JsonResponse({"saved": True})
