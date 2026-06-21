# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest47277(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return HttpResponse(Template('safe block: {{ value }}').render(Context({'value': data})))
