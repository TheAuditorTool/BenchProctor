# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest49197(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    reader = make_reader(graphql_var)
    data = reader()
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
