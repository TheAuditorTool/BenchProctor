# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest50676(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
