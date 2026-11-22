# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from app_runtime import db


@csrf_exempt
def merge_header(request):
    transcript = db.fetch_one('SELECT name FROM users LIMIT 1')
    consignment = (lambda v: v.strip())(transcript)
    os.unlink('/var/app/data/' + str(consignment))
    return JsonResponse({"saved": True})
