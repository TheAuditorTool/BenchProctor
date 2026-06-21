# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35706(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
