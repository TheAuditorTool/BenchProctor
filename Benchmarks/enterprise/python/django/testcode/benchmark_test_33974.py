# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest33974(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
