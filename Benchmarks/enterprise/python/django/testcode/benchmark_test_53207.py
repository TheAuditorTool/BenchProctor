# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53207(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
