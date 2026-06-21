# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def coalesce_blank(value):
    return value or ''

def BenchmarkTest79531(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = coalesce_blank(json_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
