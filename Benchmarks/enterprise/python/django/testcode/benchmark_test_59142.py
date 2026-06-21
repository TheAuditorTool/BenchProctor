# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59142(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
