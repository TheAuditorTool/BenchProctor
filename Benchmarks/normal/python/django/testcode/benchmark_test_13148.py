# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest13148(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
