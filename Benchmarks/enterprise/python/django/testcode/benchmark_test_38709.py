# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from lxml import etree


@dataclass
class FormData:
    payload: str

def BenchmarkTest38709(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
