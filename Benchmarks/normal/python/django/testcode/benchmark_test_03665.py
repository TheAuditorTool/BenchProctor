# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03665(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
