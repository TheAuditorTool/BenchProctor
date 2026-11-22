# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def compact_digest(request):
    headline = json.loads(request.body or b'{}').get('payload', '')
    parts = str(headline).split(',')
    remittance = ' '.join(parts)
    db.execute('SELECT * FROM "' + str(remittance).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
