# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest70914(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return JsonResponse({"saved": True})
