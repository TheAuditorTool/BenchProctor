# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


request_state: dict[str, str] = {}

def BenchmarkTest42930(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
