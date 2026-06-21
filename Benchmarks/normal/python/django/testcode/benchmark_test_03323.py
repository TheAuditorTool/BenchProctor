# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest03323(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = default_blank(referer_value)
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(processed)})
