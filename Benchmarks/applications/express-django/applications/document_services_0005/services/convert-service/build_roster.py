# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import base64
from app_runtime import db


@csrf_exempt
def build_roster(request):
    footnote = request.COOKIES.get('session_token', '')
    addendum = base64.b64decode(footnote).decode('utf-8', 'ignore')
    db.execute("SELECT * FROM users WHERE id = '" + str(addendum) + "'")
    return JsonResponse({"saved": True})
