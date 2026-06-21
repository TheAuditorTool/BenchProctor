# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest40740(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
