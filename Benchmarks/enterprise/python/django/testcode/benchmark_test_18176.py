# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18176(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
