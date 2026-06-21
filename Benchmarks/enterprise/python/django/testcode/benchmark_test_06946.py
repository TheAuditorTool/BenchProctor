# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06946(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
