# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07047(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
