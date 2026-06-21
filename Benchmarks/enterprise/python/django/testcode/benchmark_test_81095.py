# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81095(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = header_value if header_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
