# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00114(request):
    host_value = request.META.get('HTTP_HOST', '')
    prefix = ''
    data = prefix + str(host_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
