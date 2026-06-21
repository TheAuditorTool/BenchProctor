# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest20686(request):
    xml_value = request.body.decode('utf-8')
    db.execute('SELECT * FROM users WHERE id = ?', (xml_value,))
    return JsonResponse({"saved": True})
