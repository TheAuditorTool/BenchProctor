# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest71434(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JsonResponse({'error': 'privilege drop failed'}, status=500)
    return JsonResponse({"saved": True})
