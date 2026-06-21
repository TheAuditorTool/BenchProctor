# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest71269(request, path_param):
    path_value = path_param
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(path_value),))
    return JsonResponse({"saved": True})
