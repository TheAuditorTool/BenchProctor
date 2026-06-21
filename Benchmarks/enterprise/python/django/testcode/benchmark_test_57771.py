# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest57771(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
