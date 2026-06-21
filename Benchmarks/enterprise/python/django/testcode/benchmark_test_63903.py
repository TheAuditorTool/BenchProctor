# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest63903(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
