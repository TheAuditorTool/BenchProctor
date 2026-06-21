# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18217(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    return JsonResponse({'error': str(header_value), 'stack': repr(locals())}, status=500)
