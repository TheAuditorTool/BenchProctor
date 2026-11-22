# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
import json


def BenchmarkTest00251(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    resp = HttpResponse(status=302)
    resp['Location'] = str(data)
    return resp
