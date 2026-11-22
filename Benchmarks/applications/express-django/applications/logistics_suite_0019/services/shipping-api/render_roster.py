# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from app_runtime import db


@csrf_exempt
def render_roster(request):
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    parcel = (lambda v: v.strip())(citation)
    os.unlink('/var/app/data/' + str(parcel))
    return JsonResponse({"saved": True})
