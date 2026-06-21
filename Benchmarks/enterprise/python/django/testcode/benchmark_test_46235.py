# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest46235(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(origin_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = origin_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
