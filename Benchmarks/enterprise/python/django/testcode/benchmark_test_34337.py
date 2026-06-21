# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from app_runtime import db


def BenchmarkTest34337(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    subprocess.run([str(db_value), '--status'], shell=False)
    return JsonResponse({"saved": True})
