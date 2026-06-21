# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
import subprocess
from app_runtime import db


def BenchmarkTest77770(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
