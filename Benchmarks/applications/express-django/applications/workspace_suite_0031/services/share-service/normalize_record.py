# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def normalize_record(request):
    caption = json.loads(request.body or b'{}').get('payload', '')
    parts = str(caption).split(',')
    synopsis = ' '.join(parts)
    db.execute('SELECT * FROM "' + str(synopsis).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
