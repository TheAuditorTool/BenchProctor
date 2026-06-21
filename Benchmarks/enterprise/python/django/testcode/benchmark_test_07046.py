# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ctypes


def BenchmarkTest07046(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % str(json_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
