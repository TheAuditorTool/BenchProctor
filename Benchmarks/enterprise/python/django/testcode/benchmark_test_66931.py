# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


def BenchmarkTest66931(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HttpResponse(Template(processed).render(Context()))
