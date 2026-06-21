# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58118(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
