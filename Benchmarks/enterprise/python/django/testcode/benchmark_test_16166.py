# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest16166(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
