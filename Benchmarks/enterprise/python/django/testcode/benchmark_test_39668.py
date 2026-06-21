# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39668(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
