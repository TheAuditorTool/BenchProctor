# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36754(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '{}'.format(header_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
