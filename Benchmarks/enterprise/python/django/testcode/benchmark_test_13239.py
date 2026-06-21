# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest13239(request):
    xml_value = request.body.decode('utf-8')
    return HttpResponse('<!-- diagnostic build token: ' + str(xml_value) + ' -->', content_type='text/html')
