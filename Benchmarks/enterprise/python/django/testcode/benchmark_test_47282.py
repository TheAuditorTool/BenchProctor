# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest47282(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    return HttpResponse(Template(data).render(Context()))
