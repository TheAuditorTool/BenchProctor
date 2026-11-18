# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00214(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    return HttpResponse(Template('{{ value }}').render(Context({'value': data})))
