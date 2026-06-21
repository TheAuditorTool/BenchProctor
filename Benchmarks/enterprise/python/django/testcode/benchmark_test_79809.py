# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79809(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
