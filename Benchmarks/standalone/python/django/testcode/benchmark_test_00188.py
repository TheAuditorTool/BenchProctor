# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ctypes


def BenchmarkTest00188(request):
    upload_name = request.FILES['upload'].name
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
