# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00625(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
