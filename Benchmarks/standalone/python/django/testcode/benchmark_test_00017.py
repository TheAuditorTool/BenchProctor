# SPDX-License-Identifier: Apache-2.0
import os
from django.http import HttpResponse
import json


def BenchmarkTest00017(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
