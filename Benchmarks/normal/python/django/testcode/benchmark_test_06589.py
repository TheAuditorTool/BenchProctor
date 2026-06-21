# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06589(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get(str(data))
    return JsonResponse({"saved": True})
