# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest71870(request):
    upload_name = request.FILES['upload'].name
    reader = make_reader(upload_name)
    data = reader()
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
