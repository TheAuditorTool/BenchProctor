# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24584(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
