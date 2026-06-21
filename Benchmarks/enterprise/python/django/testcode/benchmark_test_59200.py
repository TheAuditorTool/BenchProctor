# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest59200(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    return redirect(str(data))
