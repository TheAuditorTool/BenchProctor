# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import ctypes


def BenchmarkTest54312(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
