# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest73181(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
