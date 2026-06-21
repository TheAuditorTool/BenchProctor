# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30463(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
