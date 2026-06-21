# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest35584(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = FormData(payload=forwarded_ip).payload
    return redirect(str(data))
