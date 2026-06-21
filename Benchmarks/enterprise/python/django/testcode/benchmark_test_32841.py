# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest32841(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    return HttpResponse(Template(data).render(Context()))
