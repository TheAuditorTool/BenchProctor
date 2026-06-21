# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66732(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
