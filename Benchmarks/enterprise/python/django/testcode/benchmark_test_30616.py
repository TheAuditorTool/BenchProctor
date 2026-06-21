# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30616(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
