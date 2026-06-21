# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02843(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
