# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest00025(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    return redirect(str(data))
