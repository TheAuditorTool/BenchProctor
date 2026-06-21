# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65714(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
