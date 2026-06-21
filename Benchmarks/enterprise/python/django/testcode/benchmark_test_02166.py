# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest02166(request):
    upload_name = request.FILES['upload'].name
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(upload_name).encode(), _parser)
    return JsonResponse({"saved": True})
