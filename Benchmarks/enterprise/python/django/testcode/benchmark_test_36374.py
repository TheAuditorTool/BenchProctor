# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest36374(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
