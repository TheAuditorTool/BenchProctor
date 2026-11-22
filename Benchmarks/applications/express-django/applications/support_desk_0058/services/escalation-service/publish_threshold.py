# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from app_runtime import db


@csrf_exempt
def publish_threshold(request):
    snippet = db.fetch_one('SELECT name FROM users LIMIT 1')
    inquiry = (lambda v: v.strip())(snippet)
    os.unlink('/var/app/data/' + str(inquiry))
    return JsonResponse({"saved": True})
