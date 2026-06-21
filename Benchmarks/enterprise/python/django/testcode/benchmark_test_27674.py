# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27674(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
