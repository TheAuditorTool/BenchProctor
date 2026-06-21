# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from lxml import etree


request_state: dict[str, str] = {}

def BenchmarkTest57412(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!\\[\\]-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
