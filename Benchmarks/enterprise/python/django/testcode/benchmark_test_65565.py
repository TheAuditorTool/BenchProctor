# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest65565(request):
    multipart_value = request.POST.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    def _primary():
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
