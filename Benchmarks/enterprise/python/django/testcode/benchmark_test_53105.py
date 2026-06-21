# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest53105(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
