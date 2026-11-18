# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import ctypes


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00438(request):
    raw_body = request.body.decode('utf-8')
    form = FormData(payload=raw_body)
    data = form.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
