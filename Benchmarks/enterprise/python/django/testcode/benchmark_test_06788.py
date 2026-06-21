# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest06788(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parts = []
    for token in str(graphql_var).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
