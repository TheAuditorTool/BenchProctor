# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def build_manifest(request):
    preface = json.loads(request.body or b'{}').get("shipping_payload", "")
    db.execute('SELECT * FROM "' + str(preface).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
