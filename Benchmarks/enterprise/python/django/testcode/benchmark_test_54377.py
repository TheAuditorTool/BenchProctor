# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import json


def BenchmarkTest54377(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
