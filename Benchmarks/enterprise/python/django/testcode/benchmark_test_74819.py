# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74819(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
