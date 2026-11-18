# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00029(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
