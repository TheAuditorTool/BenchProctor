# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse


def BenchmarkTest00052(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(processed) + '</div>')
    return resp
