# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest02635(request, path_param):
    path_value = path_param
    data = coalesce_blank(path_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
