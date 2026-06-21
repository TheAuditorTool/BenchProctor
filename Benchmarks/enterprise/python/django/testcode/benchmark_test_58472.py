# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest58472(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
