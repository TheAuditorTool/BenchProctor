# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest47862(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
