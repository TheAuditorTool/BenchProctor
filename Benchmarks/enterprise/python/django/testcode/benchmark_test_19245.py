# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest19245(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
