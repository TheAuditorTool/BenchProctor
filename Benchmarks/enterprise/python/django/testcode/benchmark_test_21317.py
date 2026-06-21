# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
from django.http import HttpResponse


def BenchmarkTest21317(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')
