# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass
from django.http import HttpResponse
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest66100(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
