# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00257(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
