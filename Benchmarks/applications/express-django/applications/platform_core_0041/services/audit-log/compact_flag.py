# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def compact_flag(request):
    passage = db.fetch_one('SELECT name FROM users LIMIT 1')
    persona = (lambda v: v.strip())(passage)
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return JsonResponse({"saved": True})
