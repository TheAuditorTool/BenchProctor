# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest53524(request):
    raw_body = request.body.decode('utf-8')
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': raw_body})))
