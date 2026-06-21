# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest16854(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
