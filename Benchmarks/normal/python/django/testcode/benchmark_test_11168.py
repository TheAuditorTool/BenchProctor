# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse
import unicodedata


@dataclass
class FormData:
    payload: str

def BenchmarkTest11168(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    normalized = unicodedata.normalize('NFKC', str(data))
    return HttpResponse('<p>' + normalized + '</p>', content_type='text/html')
