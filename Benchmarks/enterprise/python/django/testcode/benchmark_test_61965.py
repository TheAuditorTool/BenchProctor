# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import re
import json


def BenchmarkTest61965(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(Template(processed).render(Context()))
