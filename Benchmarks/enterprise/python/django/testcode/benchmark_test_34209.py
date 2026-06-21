# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest34209(request, path_param):
    path_value = path_param
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(path_value),))
    return JsonResponse({"saved": True})
