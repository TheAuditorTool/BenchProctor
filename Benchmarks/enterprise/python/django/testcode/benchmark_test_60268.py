# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest60268(request):
    xml_value = request.body.decode('utf-8')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(xml_value)))
    return JsonResponse({"saved": True})
