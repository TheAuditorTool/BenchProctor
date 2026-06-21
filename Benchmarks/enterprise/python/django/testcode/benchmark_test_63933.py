# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


request_state: dict[str, str] = {}

def BenchmarkTest63933(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
