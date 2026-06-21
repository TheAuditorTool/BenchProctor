# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest62389(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = coalesce_blank(header_value)
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.get(str(processed))
    return JsonResponse({"saved": True})
