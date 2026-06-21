# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46729(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    return JsonResponse({'error': str(referer_value), 'stack': repr(locals())}, status=500)
