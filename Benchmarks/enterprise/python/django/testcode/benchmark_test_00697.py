# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest00697(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    return redirect(str(data))
