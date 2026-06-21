# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest21189(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    return HttpResponse(str(data), content_type='text/html')
