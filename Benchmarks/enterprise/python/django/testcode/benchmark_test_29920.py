# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest29920(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    return redirect(str(data))
