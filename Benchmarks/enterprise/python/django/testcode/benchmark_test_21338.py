# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest21338(request, path_param):
    path_value = path_param
    db.execute('SELECT * FROM users WHERE id = ' + str(path_value))
    return JsonResponse({"saved": True})
