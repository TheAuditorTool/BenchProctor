# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest63504(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    return HttpResponse(Template(data).render(Context()))
