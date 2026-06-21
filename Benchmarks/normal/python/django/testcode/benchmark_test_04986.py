# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04986(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = ' '.join(str(host_value).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
