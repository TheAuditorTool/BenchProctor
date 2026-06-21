# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
from app_runtime import db


def BenchmarkTest00990(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    checked_path = os.path.join('/var/app/data', os.path.basename(db_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
