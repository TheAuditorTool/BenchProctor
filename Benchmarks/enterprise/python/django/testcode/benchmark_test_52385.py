# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest52385(request):
    xml_value = request.body.decode('utf-8')
    data = default_blank(xml_value)
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
