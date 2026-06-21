# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest77867(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
