# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56269(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
