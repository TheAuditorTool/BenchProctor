# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22976(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
