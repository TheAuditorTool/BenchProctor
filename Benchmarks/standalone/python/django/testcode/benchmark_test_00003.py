# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00003(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
