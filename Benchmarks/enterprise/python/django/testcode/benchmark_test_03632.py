# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest03632(request):
    host_value = request.META.get('HTTP_HOST', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(host_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = host_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
