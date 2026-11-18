# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def summarize_trace(request):
    caption = db.fetch_one('SELECT name FROM users LIMIT 1')
    gauge = (lambda v: v.strip())(caption)
    db.execute("SELECT * FROM users WHERE id = '" + str(gauge) + "'")
    return JsonResponse({"saved": True})
