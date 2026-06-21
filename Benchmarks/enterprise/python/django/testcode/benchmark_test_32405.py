# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest32405(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
