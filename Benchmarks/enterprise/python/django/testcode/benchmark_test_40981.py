# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from lxml import etree


def BenchmarkTest40981(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
