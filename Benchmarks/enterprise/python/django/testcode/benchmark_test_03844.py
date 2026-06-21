# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest03844(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = relay_value(origin_value)
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
