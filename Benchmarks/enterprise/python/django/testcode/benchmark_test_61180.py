# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61180(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
