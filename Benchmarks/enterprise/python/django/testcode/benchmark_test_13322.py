# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13322(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
