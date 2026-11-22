# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import json


@csrf_exempt
def attach_asset(request):
    remark = json.loads(request.body or b'{}').get("publishing_payload", "")
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "' + str(remark).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
