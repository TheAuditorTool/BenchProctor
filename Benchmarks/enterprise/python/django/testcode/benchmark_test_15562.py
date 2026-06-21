# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from app_runtime import db


def BenchmarkTest15562(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    subprocess.run('echo ' + str(comment_value), shell=True)
    return JsonResponse({"saved": True})
