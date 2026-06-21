# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest05360(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    processed = data[:64]
    with open('/var/uploads/' + str(processed), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
