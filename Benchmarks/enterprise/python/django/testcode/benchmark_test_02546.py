# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02546(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
