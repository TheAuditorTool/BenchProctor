# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69854(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
