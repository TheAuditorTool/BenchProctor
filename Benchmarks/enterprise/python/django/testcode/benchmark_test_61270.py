# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest61270(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
