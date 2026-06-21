# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22733(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
