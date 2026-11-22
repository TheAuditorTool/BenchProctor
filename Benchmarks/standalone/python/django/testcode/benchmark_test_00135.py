# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax
import json


def BenchmarkTest00135(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = str(json_value).replace('\x00', '')
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, True)
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
