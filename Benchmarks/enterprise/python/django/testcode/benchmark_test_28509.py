# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest28509(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = FormData(payload=referer_value).payload
    return redirect(str(data))
