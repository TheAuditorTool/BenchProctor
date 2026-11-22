# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def queue_retry(request):
    citation = json.loads(request.body or b'{}').get("integrations_payload", "")
    db.execute('SELECT * FROM "' + str(citation).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
