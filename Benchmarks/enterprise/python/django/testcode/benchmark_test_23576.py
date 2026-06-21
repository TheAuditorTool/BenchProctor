# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23576(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
