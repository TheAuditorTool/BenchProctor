# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

def BenchmarkTest69809(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    return HttpResponse(Template(data).render(Context()))
