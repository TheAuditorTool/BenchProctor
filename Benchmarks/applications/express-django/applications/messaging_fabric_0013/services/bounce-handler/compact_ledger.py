# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def compact_ledger(request):
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    bulletin = (lambda v: v.strip())(summary)
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return JsonResponse({"saved": True})
