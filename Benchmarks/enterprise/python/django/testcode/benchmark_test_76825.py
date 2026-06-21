# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76825(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
