# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest28201(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
