# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01670(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
