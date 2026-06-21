# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest70377(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
