# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import json


def BenchmarkTest51461(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
