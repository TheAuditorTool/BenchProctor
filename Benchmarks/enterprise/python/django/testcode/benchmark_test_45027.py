# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest45027(request):
    xml_value = request.body.decode('utf-8')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(xml_value),))
    return JsonResponse({"saved": True})
