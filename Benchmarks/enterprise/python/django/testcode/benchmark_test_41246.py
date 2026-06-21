# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41246(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
