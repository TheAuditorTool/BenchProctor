# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest02040(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
