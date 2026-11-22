# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def validate_tenant(request):
    subtitle = json.loads(request.body or b'{}').get('payload', '')
    parts = str(subtitle).split(',')
    persona = ' '.join(parts)
    db.execute('SELECT * FROM "' + str(persona).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
