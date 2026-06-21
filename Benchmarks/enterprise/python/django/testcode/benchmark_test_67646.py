# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67646(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '{}'.format(header_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
