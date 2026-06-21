# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from django.http import HttpResponse
import json


def BenchmarkTest72731(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parts = str(json_value).split(',')
    data = ','.join(parts)
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
