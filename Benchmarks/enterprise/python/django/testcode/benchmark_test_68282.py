# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest68282(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = to_text(header_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    auth_check('user', processed)
    return JsonResponse({"saved": True})
