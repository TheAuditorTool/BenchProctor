# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest76972(request):
    xml_value = request.body.decode('utf-8')
    return HttpResponse(Template(xml_value).render(Context()))
