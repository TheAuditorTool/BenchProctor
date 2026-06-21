# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest48181(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
