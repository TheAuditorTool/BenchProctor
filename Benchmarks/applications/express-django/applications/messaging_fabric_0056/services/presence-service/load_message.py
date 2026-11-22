# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def load_message(request):
    footnote = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    bulletin = normalize(footnote)
    parsed = json.loads(bulletin)
    return JsonResponse({'parsed': str(parsed)}, status=200)
