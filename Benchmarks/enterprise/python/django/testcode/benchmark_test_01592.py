# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01592(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
