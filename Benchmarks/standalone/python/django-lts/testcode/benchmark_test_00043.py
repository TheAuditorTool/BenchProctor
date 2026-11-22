# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from pathlib import Path


def BenchmarkTest00043(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
