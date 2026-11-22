# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00195(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    form = FormData(payload=referer_value)
    data = form.payload
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return JsonResponse({'allocated': len(records)}, status=200)
