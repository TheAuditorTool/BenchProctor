# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13197(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
