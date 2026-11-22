# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import xml.sax


def BenchmarkTest00082(request):
    field_value = request.POST.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, True)
    parser.setContentHandler(xml.sax.ContentHandler())
    parser.parse(io.StringIO(str(data)))
    return JsonResponse({"saved": True})
