# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest79046(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    eval(compile("_resp = requests.get(str(data))\ndb.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
