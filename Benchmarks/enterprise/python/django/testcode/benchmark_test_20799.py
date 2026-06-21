# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from django.http import HttpResponse
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest20799(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
