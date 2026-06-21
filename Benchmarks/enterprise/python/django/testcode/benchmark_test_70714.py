# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest70714(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
