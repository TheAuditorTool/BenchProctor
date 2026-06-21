# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
import json
from types import SimpleNamespace


def BenchmarkTest72001(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return HttpResponse(mark_safe('<img src="' + str(processed) + '">'))
