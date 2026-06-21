# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03348(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
