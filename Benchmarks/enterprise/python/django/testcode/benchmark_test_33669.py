# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest33669(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    return HttpResponse(Template(data).render(Context()))
