# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def BenchmarkTest10933(request):
    multipart_value = request.POST.get('multipart_field', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(multipart_value).encode(), _parser)
    return JsonResponse({"saved": True})
