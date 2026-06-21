# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39738(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    prefix = ''
    data = prefix + str(header_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
