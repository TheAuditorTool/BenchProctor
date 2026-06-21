# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19403(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
