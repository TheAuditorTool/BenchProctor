# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest18650(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
