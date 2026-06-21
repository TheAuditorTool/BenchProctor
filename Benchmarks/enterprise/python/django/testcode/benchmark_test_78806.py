# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from app_runtime import db


def BenchmarkTest78806(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JsonResponse({'wrapped': wrapped}, status=200)
