# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest08538(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    if graphql_var not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = graphql_var
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return JsonResponse({"saved": True})
