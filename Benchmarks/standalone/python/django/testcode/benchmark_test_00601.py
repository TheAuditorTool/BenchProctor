# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00601(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
