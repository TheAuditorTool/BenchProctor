# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def query_dashboard(request):
    quotation = json.loads(request.body or b'{}').get("telemetry_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(quotation) + "'")
    return JsonResponse({"saved": True})
