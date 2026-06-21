# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import time


request_state: dict[str, str] = {}

def BenchmarkTest33056(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
    return JsonResponse({"saved": True})
