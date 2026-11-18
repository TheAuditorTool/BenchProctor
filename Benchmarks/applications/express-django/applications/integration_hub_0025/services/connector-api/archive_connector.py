# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


@csrf_exempt
def archive_connector(request):
    footnote = db.fetch_one('SELECT name FROM users LIMIT 1')
    handshake = (lambda v: v.strip())(footnote)
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return JsonResponse({"saved": True})
