# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest64189(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
