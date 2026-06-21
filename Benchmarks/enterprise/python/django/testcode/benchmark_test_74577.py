# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


request_state: dict[str, str] = {}

def BenchmarkTest74577(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-{}()=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    eval(str(processed))
    return JsonResponse({"saved": True})
