# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


request_state: dict[str, str] = {}

def BenchmarkTest62457(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)
