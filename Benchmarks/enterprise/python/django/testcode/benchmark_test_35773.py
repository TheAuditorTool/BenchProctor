# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
from lxml import etree


def BenchmarkTest35773(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
