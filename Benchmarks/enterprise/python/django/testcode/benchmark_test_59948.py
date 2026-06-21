# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse


def BenchmarkTest59948(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
