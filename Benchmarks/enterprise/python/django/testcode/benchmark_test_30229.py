# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest30229(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    eval(compile("with open('/var/uploads/' + str(data), 'wb') as fh:\n    fh.write(b'data')", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
