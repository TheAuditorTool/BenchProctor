# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75296(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
