# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html


request_state: dict[str, str] = {}

def BenchmarkTest23866(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
