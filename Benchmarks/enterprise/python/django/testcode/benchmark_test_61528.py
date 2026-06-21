# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest61528(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
