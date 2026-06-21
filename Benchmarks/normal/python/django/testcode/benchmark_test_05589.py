# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05589(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
