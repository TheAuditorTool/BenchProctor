# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
from django.http import HttpResponse


def BenchmarkTest49045(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
