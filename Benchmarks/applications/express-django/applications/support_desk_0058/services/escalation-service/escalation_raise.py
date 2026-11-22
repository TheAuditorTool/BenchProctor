# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import json


@csrf_exempt
def raise_escalation(request):
    memo = json.loads(request.body or b'{}').get("support_payload", "")
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(memo) + "'")
    return JsonResponse({"saved": True})
