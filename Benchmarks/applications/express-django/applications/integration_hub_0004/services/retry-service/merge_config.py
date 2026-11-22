# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def merge_config(request):
    summary = json.loads(request.body or b'{}').get('payload', '')
    parts = str(summary).split(',')
    handshake = ' '.join(parts)
    db.execute('SELECT * FROM "' + str(handshake).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
