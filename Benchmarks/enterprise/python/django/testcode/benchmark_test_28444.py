# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest28444(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = relay_value(header_value)
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(processed)})
