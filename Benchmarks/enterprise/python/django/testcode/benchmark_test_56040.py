# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from dataclasses import dataclass
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest56040(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
