# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest00165(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
