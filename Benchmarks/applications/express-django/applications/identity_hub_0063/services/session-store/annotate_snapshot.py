# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def annotate_snapshot(request):
    paragraph = db.fetch_one('SELECT name FROM users LIMIT 1')
    persona = (lambda v: v.strip())(paragraph)
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return JsonResponse({"saved": True})
