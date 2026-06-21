# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


request_state: dict[str, str] = {}

def BenchmarkTest09811(request):
    multipart_value = request.POST.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
