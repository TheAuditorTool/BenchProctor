# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09000(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
