# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re
import json


def relay_value(value):
    return value

def BenchmarkTest60226(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    if not re.fullmatch('^[\\w\\s<>\\"\'/(){}.*]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
