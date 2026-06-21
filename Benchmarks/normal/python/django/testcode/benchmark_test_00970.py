# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00970(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
