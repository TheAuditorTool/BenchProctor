# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62879(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
