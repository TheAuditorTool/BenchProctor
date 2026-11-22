# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax
import defusedxml.sax


def BenchmarkTest00060(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    parser = defusedxml.sax.make_parser()
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
