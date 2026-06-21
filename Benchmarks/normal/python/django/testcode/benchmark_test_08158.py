# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest08158(request):
    xml_value = request.body.decode('utf-8')
    return HttpResponse('<html><body><h1>' + str(xml_value) + '</h1></body></html>', content_type='text/html')
