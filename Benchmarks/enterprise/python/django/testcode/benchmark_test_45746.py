# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest45746(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
