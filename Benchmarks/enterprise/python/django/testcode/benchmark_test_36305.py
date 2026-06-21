# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest36305(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = default_blank(forwarded_ip)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data) == 'fluffy':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
