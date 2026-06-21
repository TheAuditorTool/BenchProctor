# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest34597(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
