# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest20225(request, path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
