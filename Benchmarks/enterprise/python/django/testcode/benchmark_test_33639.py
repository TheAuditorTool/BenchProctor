# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest33639(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    return HttpResponse(Template(data).render(Context()))
