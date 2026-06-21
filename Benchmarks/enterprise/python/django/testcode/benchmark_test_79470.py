# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import os
import asyncio
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest79470(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    async def _evasion_task():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return HttpResponse(content)
    return asyncio.run(_evasion_task())
