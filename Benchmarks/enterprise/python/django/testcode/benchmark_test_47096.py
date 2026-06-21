# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
import subprocess
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest47096(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
