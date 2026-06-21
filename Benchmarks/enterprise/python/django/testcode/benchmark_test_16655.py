# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


def BenchmarkTest16655(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    return HttpResponse(Template(graphql_var).render(Context()))
