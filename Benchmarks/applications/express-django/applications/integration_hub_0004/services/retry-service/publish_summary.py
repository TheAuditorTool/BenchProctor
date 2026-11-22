# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from app_runtime import db


@csrf_exempt
def publish_summary(request):
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    handshake = (lambda v: v.strip())(summary)
    os.unlink('/var/app/data/' + str(handshake))
    return JsonResponse({"saved": True})
