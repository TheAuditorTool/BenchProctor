# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest54291(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
