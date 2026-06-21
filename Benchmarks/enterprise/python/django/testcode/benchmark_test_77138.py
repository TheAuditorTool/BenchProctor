# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest77138(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
