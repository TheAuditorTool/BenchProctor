# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest39349(request):
    xml_value = request.body.decode('utf-8')
    return HttpResponse('<script src="' + str(xml_value) + '"></script>', content_type='text/html')
