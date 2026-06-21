# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from app_runtime import db


def BenchmarkTest15079(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
