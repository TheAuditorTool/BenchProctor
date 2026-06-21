# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04892(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
