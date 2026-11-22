# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
from lxml import etree
import base64


def BenchmarkTest00067(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    for _event, element in etree.iterparse(io.BytesIO(str(data).encode()), events=('end',), load_dtd=True, resolve_entities=True, no_network=False):
        element.clear()
    return JsonResponse({"saved": True})
