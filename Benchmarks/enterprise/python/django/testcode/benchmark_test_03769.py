# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from app_runtime import db


def BenchmarkTest03769(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
