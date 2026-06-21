# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest08022(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    return HttpResponse(Template(data).render(Context()))
