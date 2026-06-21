# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12322(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
