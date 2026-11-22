# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax


def BenchmarkTest00147(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, True)
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
