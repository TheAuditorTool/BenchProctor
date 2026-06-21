# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest77586(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
