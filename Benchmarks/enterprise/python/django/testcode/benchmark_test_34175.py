# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest34175(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
