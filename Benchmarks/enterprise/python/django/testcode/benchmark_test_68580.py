# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68580(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
