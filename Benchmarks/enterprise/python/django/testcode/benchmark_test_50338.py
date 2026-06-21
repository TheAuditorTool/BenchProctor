# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import db


def BenchmarkTest50338(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(ua_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = ua_value
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return JsonResponse({"saved": True})
