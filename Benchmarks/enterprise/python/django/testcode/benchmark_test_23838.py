# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
from types import SimpleNamespace


def BenchmarkTest23838(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    os.environ['APP_USER_PREFERENCE'] = str(data)
    return JsonResponse({'config_set': 'APP_USER_PREFERENCE'}, status=200)
