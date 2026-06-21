# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import pickle


def BenchmarkTest42454(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
