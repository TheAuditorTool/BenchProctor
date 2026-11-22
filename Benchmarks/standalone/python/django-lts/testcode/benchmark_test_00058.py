# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest00058(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
