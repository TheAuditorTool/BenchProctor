# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax


def BenchmarkTest00082(request):
    multipart_value = request.POST.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, True)
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
