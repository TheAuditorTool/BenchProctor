# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest20477(request):
    xml_value = request.body.decode('utf-8')
    return HttpResponse(mark_safe('<img src="' + str(xml_value) + '">'))
