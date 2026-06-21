# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html


request_state: dict[str, str] = {}

def BenchmarkTest42880(request):
    multipart_value = request.POST.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
