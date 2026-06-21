# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30895(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    return HttpResponse(str(data), content_type='text/html')
