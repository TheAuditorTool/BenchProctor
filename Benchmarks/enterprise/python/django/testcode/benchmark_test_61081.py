# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64
from django.http import HttpResponse


def BenchmarkTest61081(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
