# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def prune_record(request):
    excerpt = json.loads(request.body or b'{}').get('payload', '')
    parts = str(excerpt).split(',')
    cohort = ' '.join(parts)
    db.execute('SELECT * FROM "' + str(cohort).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
