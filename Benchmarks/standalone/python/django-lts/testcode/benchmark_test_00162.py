# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00162(request):
    multipart_value = request.POST.get('multipart_field', '')
    form = FormData(payload=multipart_value)
    data = form.payload
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, True)
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
