# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def search_knowledge(request):
    excerpt = json.loads(request.body or b'{}').get("support_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(excerpt) + "'")
    return JsonResponse({"saved": True})
