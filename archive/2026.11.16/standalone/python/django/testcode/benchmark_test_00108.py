# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00108(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    form = FormData(payload=db_value)
    data = form.payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
