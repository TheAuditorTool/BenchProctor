# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest24577(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = FormData(payload=json_value).payload
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
