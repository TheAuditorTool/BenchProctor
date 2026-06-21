# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest76162(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
