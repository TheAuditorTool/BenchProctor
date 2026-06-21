# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def coalesce_blank(value):
    return value or ''

def BenchmarkTest50203(request):
    upload_name = request.FILES['upload'].name
    data = coalesce_blank(upload_name)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
