# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
from lxml import etree


def BenchmarkTest10036(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
