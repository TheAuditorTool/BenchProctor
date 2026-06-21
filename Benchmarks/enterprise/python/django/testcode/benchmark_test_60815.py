# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest60815(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
