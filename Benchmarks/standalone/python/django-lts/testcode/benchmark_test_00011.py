# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import ctypes


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00011(request):
    host_value = request.META.get('HTTP_HOST', '')
    form = FormData(payload=host_value)
    data = form.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
