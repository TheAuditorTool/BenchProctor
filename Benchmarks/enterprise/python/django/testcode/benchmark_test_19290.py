# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest19290(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body:.200s}'
    return HttpResponse(Template(data).render(Context()))
