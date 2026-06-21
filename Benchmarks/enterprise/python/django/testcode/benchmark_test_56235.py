# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import ctypes


def BenchmarkTest56235(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
