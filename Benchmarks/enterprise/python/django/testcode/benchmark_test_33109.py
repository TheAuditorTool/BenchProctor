# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest33109(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
