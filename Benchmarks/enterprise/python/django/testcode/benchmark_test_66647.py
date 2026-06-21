# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66647(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
