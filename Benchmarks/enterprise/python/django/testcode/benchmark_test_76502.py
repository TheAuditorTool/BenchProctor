# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest76502(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    return HttpResponse(Template(data).render(Context()))
