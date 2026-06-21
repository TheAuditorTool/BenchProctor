# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re
import json


def BenchmarkTest77239(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
