# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


def BenchmarkTest46492(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    return HttpResponse(Template(data).render(Context()))
