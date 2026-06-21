# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest53813(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
