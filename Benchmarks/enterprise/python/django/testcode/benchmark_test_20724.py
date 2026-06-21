# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from app_runtime import db


def BenchmarkTest20724(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
