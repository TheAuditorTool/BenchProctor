# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest30128(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
