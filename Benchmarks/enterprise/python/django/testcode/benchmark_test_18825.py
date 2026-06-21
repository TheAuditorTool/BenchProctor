# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18825(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
