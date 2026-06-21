# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def relay_value(value):
    return value

def BenchmarkTest39502(request):
    raw_body = request.body.decode('utf-8')
    data = relay_value(raw_body)
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
