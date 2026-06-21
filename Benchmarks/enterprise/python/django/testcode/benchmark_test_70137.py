# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html


def ensure_str(value):
    return str(value)

def BenchmarkTest70137(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ensure_str(host_value)
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
