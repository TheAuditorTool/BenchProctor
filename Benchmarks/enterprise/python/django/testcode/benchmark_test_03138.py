# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest03138(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    return HttpResponse(str(data), content_type='text/html')
