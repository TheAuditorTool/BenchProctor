# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from lxml import etree


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00686(request):
    multipart_value = request.POST.get('multipart_field', '')
    form = FormData(payload=multipart_value)
    data = form.payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
