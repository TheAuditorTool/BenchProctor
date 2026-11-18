# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00493(request):
    upload_name = request.FILES['upload'].name
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(upload_name).strip()
        case _:
            data = str(upload_name)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
