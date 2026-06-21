# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest49576(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(graphql_var),))
    return JsonResponse({"saved": True})
