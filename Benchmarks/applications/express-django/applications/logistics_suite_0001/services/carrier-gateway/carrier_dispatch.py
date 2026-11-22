# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import json


@csrf_exempt
def dispatch_carrier(request):
    paragraph = json.loads(request.body or b'{}').get("shipping_payload", "")
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '" + str(paragraph) + "'")
    return JsonResponse({"saved": True})
