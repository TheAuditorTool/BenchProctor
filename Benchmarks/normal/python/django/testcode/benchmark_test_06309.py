# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest06309(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JsonResponse({'secret': str(secret)}, status=200)
