# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def BenchmarkTest00049(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return JsonResponse({'allocated': len(records)}, status=200)
