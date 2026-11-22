# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
from lxml import etree


def BenchmarkTest00215(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    for _event, element in etree.iterparse(io.BytesIO(str(data).encode()), events=('end',), load_dtd=True, resolve_entities=True, no_network=False):
        element.clear()
    return JsonResponse({"saved": True})
