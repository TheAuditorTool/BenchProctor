# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63389(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(auth_header)})
