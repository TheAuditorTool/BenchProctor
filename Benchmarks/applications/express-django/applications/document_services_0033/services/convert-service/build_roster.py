# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app_runtime import db


@csrf_exempt
def build_roster(request):
    snippet = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    addendum = normalize(snippet)
    parsed = json.loads(addendum)
    return JsonResponse({'parsed': str(parsed)}, status=200)
