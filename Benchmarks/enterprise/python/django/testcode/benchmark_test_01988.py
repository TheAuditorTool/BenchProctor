# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01988(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
