# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest37519(request):
    raw_body = request.body.decode('utf-8')
    data = coalesce_blank(raw_body)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if str(processed) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
