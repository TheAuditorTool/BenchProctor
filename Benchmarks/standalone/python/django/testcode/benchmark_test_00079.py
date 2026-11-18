# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import re


def BenchmarkTest00079(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
