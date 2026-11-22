# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from pathlib import Path


def BenchmarkTest00152(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if not re.fullmatch("^(asc|desc|name|created)$", str(cookie_value)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = cookie_value
    Path('/var/app/data/' + str(processed)).write_text('data')
    return JsonResponse({"saved": True})
