# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest02746(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    return HttpResponse(Template(data).render(Context()))
