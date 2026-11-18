# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def pull_supplier_feed(request):
    summary = json.loads(request.body or b'{}').get("inventory_payload", "")
    db.execute('SELECT * FROM users WHERE id = :id', {'id': summary})
    return JsonResponse({"saved": True})
