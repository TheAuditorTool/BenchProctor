# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest57075(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
