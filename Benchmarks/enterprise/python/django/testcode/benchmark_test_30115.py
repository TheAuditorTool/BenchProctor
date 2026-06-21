# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from app_runtime import db


def BenchmarkTest30115(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
