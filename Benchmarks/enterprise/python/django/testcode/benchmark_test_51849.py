# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51849(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
