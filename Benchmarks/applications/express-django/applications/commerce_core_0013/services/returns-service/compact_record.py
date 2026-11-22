# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from app_runtime import db


@csrf_exempt
def compact_record(request):
    wording = db.fetch_one('SELECT name FROM users LIMIT 1')
    backorder = (lambda v: v.strip())(wording)
    os.unlink('/var/app/data/' + str(backorder))
    return JsonResponse({"saved": True})
