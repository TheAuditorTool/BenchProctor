# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def validate_policy(request):
    quotation = json.loads(request.body or b'{}').get('payload', '')
    parts = str(quotation).split(',')
    parcel = ' '.join(parts)
    db.execute('SELECT * FROM "' + str(parcel).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
