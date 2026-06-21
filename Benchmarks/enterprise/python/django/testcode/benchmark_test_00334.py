# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ctypes


def BenchmarkTest00334(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json.loads(json_value).get('value', '')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
