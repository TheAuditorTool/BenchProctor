# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest35649(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(forwarded_ip)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = forwarded_ip
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
