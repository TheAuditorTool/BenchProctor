# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest48624(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    return HttpResponse(str(data), content_type='text/html')
