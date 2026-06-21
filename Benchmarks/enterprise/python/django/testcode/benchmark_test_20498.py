# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20498(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
