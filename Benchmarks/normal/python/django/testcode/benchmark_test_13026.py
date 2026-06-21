# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json


def BenchmarkTest13026(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    return HttpResponse(mark_safe('<div>' + str(graphql_var) + '</div>'))
