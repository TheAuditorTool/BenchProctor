# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


request_state: dict[str, str] = {}

def BenchmarkTest17615(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
