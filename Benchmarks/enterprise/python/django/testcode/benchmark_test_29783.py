# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest29783(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    processed = data[:64]
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
