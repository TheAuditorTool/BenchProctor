# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
import json


def BenchmarkTest00041(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
