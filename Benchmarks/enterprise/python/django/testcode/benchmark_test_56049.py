# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest56049(request, path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return JsonResponse({"saved": True})
