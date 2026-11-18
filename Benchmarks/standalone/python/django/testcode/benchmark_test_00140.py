# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00140(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    form = FormData(payload=graphql_var)
    data = form.payload
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
