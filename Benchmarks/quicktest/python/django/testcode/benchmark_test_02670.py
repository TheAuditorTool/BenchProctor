# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02670(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    json.loads(data)
    return JsonResponse({"saved": True})
