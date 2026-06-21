# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest40787(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = FormData(payload=auth_header).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
