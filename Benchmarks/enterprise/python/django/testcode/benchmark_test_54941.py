# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from app_runtime import db


def BenchmarkTest54941(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    subprocess.run([str(comment_value), '--status'], shell=False)
    return JsonResponse({"saved": True})
