# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40087(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
