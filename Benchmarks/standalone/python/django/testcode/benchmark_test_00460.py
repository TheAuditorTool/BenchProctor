# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00460(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
