# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62031(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
