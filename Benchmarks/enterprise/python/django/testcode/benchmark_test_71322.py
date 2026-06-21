# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest71322(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
