# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


request_state: dict[str, str] = {}

def BenchmarkTest25807(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
