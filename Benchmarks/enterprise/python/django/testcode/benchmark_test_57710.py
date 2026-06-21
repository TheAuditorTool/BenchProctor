# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest57710(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
