# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def to_text(value):
    return str(value).strip()

def BenchmarkTest55478(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = to_text(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['user'] = str(processed)
    return JsonResponse({"saved": True})
