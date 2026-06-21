# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest62319(request):
    raw_body = request.body.decode('utf-8')
    data = ensure_str(raw_body)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
