# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06863(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
