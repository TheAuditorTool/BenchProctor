# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest01595(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
