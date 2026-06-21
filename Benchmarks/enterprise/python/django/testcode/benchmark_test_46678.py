# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest46678(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    eval(compile("_resp = requests.get(str(data))\ndb.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
