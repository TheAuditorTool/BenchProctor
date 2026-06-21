# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest19758(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    with open('/var/uploads/' + str(graphql_var), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
