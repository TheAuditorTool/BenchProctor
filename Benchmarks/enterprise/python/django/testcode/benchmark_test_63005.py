# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63005(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
