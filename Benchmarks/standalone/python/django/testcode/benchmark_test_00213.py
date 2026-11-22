# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax
import defusedxml.sax


def BenchmarkTest00213(request):
    field_value = request.POST.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
