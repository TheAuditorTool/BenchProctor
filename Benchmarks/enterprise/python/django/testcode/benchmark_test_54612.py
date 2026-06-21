# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54612(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
