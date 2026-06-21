# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27468(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = str(header_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
