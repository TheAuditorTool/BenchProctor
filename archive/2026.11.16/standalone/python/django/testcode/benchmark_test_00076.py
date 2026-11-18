# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import ctypes


def BenchmarkTest00076(request):
    field_value = request.POST.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
