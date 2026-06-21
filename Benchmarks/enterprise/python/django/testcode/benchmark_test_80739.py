# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80739(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(referer_value)})
