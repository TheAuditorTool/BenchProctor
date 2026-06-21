# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import pickle


def BenchmarkTest50376(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
