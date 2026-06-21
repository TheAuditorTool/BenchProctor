# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest06078(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
