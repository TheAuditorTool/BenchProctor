# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
import subprocess
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest09163(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
