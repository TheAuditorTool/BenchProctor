# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60488(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
