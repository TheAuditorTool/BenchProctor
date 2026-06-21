# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


def normalise_input(value):
    return value.strip()

def BenchmarkTest47556(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = normalise_input(forwarded_ip)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.setuid(int(str(processed)) if str(processed).isdigit() else 0)
    return JsonResponse({"saved": True})
