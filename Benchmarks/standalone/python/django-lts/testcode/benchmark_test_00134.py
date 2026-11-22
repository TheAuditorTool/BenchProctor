# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00134(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(processed) + '</div>')
    return resp
