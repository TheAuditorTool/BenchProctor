# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax
import defusedxml.sax
import json


def BenchmarkTest00078(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
