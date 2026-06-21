# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32368(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
