# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from app_runtime import db


def BenchmarkTest20925(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
