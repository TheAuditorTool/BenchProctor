# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67578(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
