# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60121(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
